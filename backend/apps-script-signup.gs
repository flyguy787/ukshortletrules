// Google Apps Script web app: receives signups from ukshortletrules.co.uk and adds them to Resend.
// The Resend API key lives ONLY in Script Properties (never in this file or the website).
// Setup: Project Settings -> Script Properties: RESEND_API_KEY = <key>, RESEND_SEGMENT_ID = e5cdf8c4-dad7-4448-99d9-13bed82ae802
function doPost(e) {
  var email = String((e.parameter && e.parameter.email) || '').trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length > 254) return out_('invalid');
  var cache = CacheService.getScriptCache();               // crude rate-limit: one attempt per email per 10 min
  if (cache.get(email)) return out_('ok'); cache.put(email, '1', 600);
  var p = PropertiesService.getScriptProperties();
  var res = UrlFetchApp.fetch('https://api.resend.com/contacts', {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + p.getProperty('RESEND_API_KEY') },
    payload: JSON.stringify({ email: email, unsubscribed: false,
      segments: [{ id: p.getProperty('RESEND_SEGMENT_ID') }] })
  });
  console.log(res.getResponseCode() + ' ' + res.getContentText().slice(0, 200));
  return out_('ok');
}
function out_(s) { return ContentService.createTextOutput(JSON.stringify({ status: s })).setMimeType(ContentService.MimeType.JSON); }
