# ---- /changes: 'What changed in your council?' picker (growth push, 2 Nov) ----
# Shared RCPICK (guidehub.py): pick a council (council:<slug>) or a whole nation (nation:<id>) -> its one-line rule (data.json rule / nation summary),
# its latest 2 logged changes from this page's own log (council: entries this page already links to that council via _chcouncils; nation: entries
# tagged with that nation), its next sourced key dates, a link to its page (data-cta changes-council-page) and an in-context alert box pre-set to the
# pick (data-cta changes-council-result). While shown it hides both generic boxes (top-answer and sitewide, .alertcta); the placeholder restores them.
# Perth & Kinross (PICK_EXCL) never appears. GA4: changes_council_pick {area_type, council}, once per distinct pick per page view. No new facts.
def _chslugs(t):
    return [re.search(r'councils/([a-z0-9-]+)\.html',h).group(1) for h in _chcouncils(t)]
_cch={}
for _c in _chsorted:
    _ln=_dt0.date.fromisoformat(_c['date']).strftime('%-d %b %Y')+': '+_c['text']
    for _s in _chslugs(_c['text']):_cch.setdefault(('c',_s),[]).append(_ln)
    for _n in d['nations']:
        if _n['name'] in _c['nation'].split('/'):_cch.setdefault(('n',_n['id']),[]).append(_ln)
_cch={k:v[:2] for k,v in _cch.items()}
assert not any('kinross' in k[1] for k in _cch)
CCPICK=RCPICK('cc','changes-council-result','changes-council-page','changes_council_pick','What changed in your council?',
  'Pick your council, or a whole nation, to see its rules in brief and its latest logged changes, with free alerts when the next one happens.',ch=_cch,hide='.alertcta')
_CHPAGE(CCPICK)
