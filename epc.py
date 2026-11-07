# ---- Guide: EPC and energy rules (MEES) for short-term / holiday lets (England & Wales) ----
# Facts checked 7 Nov 2026 against GOV.UK. Anything else marked UNVERIFIED.
import json as _j
MEES_RESP='https://www.gov.uk/government/consultations/improving-the-energy-performance-of-privately-rented-homes-2025-update/outcome/improving-the-energy-performance-of-privately-rented-homes-government-response-html'
EPC_REFORM='https://www.gov.uk/government/consultations/reforms-to-the-energy-performance-of-buildings-regime'
SELF_CAT='https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'
EPC_DWELL='https://www.gov.uk/buy-sell-your-home/energy-performance-certificates'
MEES_LANDLORD='https://www.gov.uk/guidance/domestic-private-rented-property-minimum-energy-efficiency-standard-landlord-guidance'
EPC_FIND='https://www.gov.uk/find-energy-certificate'
_CHECKED='7 Nov 2026'
f='epc-energy-rules-holiday-lets.html'
t='EPC and energy rules for holiday lets'
dsc='EPC and MEES for UK holiday lets and short-term lets: short-term lets are not in the 2030 PRS energy standard for now (under review), when you still need an EPC, and what England and Wales landlords must do. Official sources.'
EQ=[('Do short-term lets have to meet the new 2030 PRS energy standard?','No, not at this time. In its 21 January 2026 response on improving the energy performance of privately rented homes, the government said short-term lets will not be required to comply with PRS MEES for now. That position remains under review. The government will seek legislative power for the Secretary of State to bring short-term lets into scope later if needed, and commits to seek views on how such a policy could be tailored before deciding.'),
 ('What is the higher MEES standard for long-term private rented homes?','For privately rented homes in England and Wales, government will raise minimum energy efficiency standards using new EPC metrics (a dual-metric fabric-first approach described as delivering outcomes similar to EPC C). Landlords must invest up to £10,000 per property. All tenancies in scope must comply by 1 October 2030. The existing EPC E minimum continues until then.'),
 ('Does my holiday let need an EPC today?','It depends. GOV.UK self-catering guidance for England says you must check whether you need an EPC, and points to the Energy Performance Certificates guidance. That guidance says you normally need an EPC when selling or renting out a dwelling, but lists exceptions that can cover some holiday accommodation — including holiday accommodation rented out for less than 4 months a year, or let under a licence to occupy. There is no blanket "every holiday let must reach EPC C" rule on those pages. Use the official guidance and the find-an-energy-certificate service.'),
 ('Is there a rule that holiday lets must reach EPC C?','Not for short-term lets under the PRS MEES response. The higher 2030 standard (EPC C-equivalent against new metrics, £10,000 cost cap) is for the domestic private rented sector in England and Wales. Short-term lets are out of scope for now, under review. Do not treat long-term PRS MEES as if it already applied to holiday lets.'),
 ('What is changing about EPCs themselves?','Government published a partial response to reforms of the Energy Performance of Buildings regime. New headline metrics will appear on reformed domestic EPCs. An update on 9 March 2026 moved the launch of reformed domestic EPCs to the second half of 2027 (later than the earlier target), while government works with industry on a shared plan.'),
 ('Does this apply in Scotland or Northern Ireland?','The higher PRS MEES policy described on this page is for England and Wales under the PRS Regulations. Scotland and Northern Ireland have their own energy and EPC frameworks. Short-let treatment there is not verified in detail on this page — check local official rules. Scotland short-term let licensing often asks for an EPC for whole-house or flat lets; see our Scotland licence guide.'),
 ('I also let long-term as a private landlord. What should I do?','If you let on a relevant long-term tenancy that is within the domestic PRS MEES rules in England or Wales, the existing EPC E minimum still applies, and the higher standard must be met for all such tenancies by 1 October 2030 (subject to exemptions and Parliamentary approval of the legislative steps). Read the domestic PRS landlord guidance and the January 2026 government response. Short-term holiday use is treated separately for now.'),
 ('What should hosts watch for next?','Any decision to bring short-term lets into PRS MEES (still under review), the primary and secondary legislation for the higher PRS standard, reformed domestic EPC launch in the second half of 2027, and updates to GOV.UK self-catering and EPC guidance. Sign up below for alerts when the short-let energy or MEES position changes.'),
 ('Is this legal advice?','No. This page is general information from GOV.UK sources checked on 7 November 2026. Energy and letting rules depend on how you let the property. Confirm with the linked official guidance and a qualified adviser before acting.')]
_eld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in EQ]}).replace('</','<\\/')
_efq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in EQ)
_ES=[('DESNZ: Improving the energy performance of privately rented homes — government response (HTML, updated 21 Jan 2026)',MEES_RESP),
     ('MHCLG / DESNZ: Reforms to the Energy Performance of Buildings regime (partial response; update 9 Mar 2026)',EPC_REFORM),
     ('GOV.UK: Letting out a self-catering holiday home in England — rules and regulations (EPC where needed)',SELF_CAT),
     ('GOV.UK: Energy Performance Certificates (when you need one; holiday-accommodation exceptions)',EPC_DWELL),
     ('GOV.UK: Domestic private rented property minimum energy efficiency standard — landlord guidance (EPC E)',MEES_LANDLORD),
     ('GOV.UK: Find an energy certificate',EPC_FIND)]
b=f'''<p class="lead">Hosts often ask whether holiday lets must hit EPC C by 2030. For England and Wales, the official answer today is: the higher private-rented MEES standard is aimed at long-term tenancies, short-term lets are <b>not required to comply at this time</b> (the position remains under review), and you may still need an EPC in some cases — but not under a blanket "holiday let = EPC C" rule.</p>
{TLDR([f'<b>Short-term lets:</b> not required to comply with PRS MEES at this time; position <b>under review</b> (<a href="{MEES_RESP}" rel="nofollow">government response, 21 Jan 2026</a>).',
 f'<b>Long-term PRS (England &amp; Wales):</b> higher dual-metric standard (EPC C-equivalent outcomes), invest up to £10,000 per property; all tenancies by <b>1 October 2030</b>. Existing EPC E minimum continues until then.',
 f'<b>When you may still need an EPC:</b> GOV.UK says check — selling or renting a dwelling normally needs one; some holiday accommodation is listed as exempt (for example under 4 months a year, or a licence to occupy). See <a href="{EPC_DWELL}" rel="nofollow">EPC guidance</a> and <a href="{SELF_CAT}" rel="nofollow">self-catering rules</a>.',
 f'<b>Do now:</b> do not assume the 2030 PRS standard already applies to your short let; check whether you need an EPC for sale/marketing/licensing; <a href="#epc-energy-alert">get alerts</a> if the short-let MEES position changes.'],
 title='In short: EPC and MEES for holiday lets',sub='From GOV.UK. Not legal advice. England and Wales MEES focus.')}
{SCARDS([('Short-term lets','in','Not in PRS MEES for now','Government response: STLs not required to comply at this time.','applies'),
 ('Under review','proposed','May be brought in later','SoS power + tailored consultation before any decision.','watch'),
 ('PRS long-term','coming','Higher standard by 1 Oct 2030','Up to £10,000; dual-metric / C-equivalent. EPC E until then.','prs'),
 ('EPC reform','coming','New domestic EPCs in H2 2027','Launch moved (update 9 Mar 2026); shared industry plan.','epc-reform')])}
{TOC([('applies','Does this apply to my holiday let?'),('prs','What the 2030 PRS standard is'),('when-epc','When you may still need an EPC'),('watch','What is under review'),('scotland-ni','Scotland and Northern Ireland'),('hosts','What hosts should do now'),('epc-energy-alert','Get EPC / MEES alerts'),('faq','Questions'),('sources','Sources')])}
<h2 id="applies">1. Does this apply to my holiday let?</h2>
<p>For <b>England and Wales</b> short-term / holiday lets used as guest accommodation rather than a long-term private tenancy:</p>
<ul class="tick"><li><b>Higher PRS MEES (the 2030 energy upgrade rules):</b> <b>not required at this time</b>. The government response on improving the energy performance of privately rented homes says short-term lets will not have to comply with PRS MEES for now (<a href="{MEES_RESP}" rel="nofollow">GOV.UK, updated 21 Jan 2026</a>).</li>
<li><b>That position remains under review.</b> Government will seek legislative power for the Secretary of State to bring short-term lets into scope later if necessary, and commits to seek views on how such a policy can be tailored before deciding.</li>
<li><b>Having or needing an EPC</b> is a separate question from MEES compliance. GOV.UK self-catering guidance says you must check whether you need an EPC (<a href="{SELF_CAT}" rel="nofollow">self-catering rules</a>).</li></ul>
{CALLOUT(f'<p>If you only run short-term holiday lets in England or Wales, do <b>not</b> treat the 1 October 2030 PRS MEES deadline as applying to those lets today. If you also let long-term on a relevant private tenancy, the PRS rules can still apply to that tenancy — see section 2.</p>',title='What this means for hosts')}
<h2 id="prs">2. What the 2030 PRS standard is (for contrast)</h2>
<p>This section is for hosts who also let long-term, or who need to understand what STLs are currently carved out of.</p>
<ul class="tick"><li>Applies to the <b>domestic private rented sector in England and Wales</b> under the PRS Regulations (<a href="{MEES_RESP}" rel="nofollow">government response</a>).</li>
<li><b>Higher standard:</b> dual-metric standard against new EPC metrics (primary fabric performance, then a secondary smart-readiness or heating-system metric at the landlord\'s discretion), designed to deliver fuel-poverty and bill outcomes similar to an EPC C standard against the existing metric.</li>
<li><b>Cost cap:</b> landlords invest up to <b>£10,000</b> per property on relevant improvements; if the property is still below the standard after that, a cost-cap exemption can be registered (details in the response).</li>
<li><b>Deadline:</b> all tenancies in scope must comply by <b>1 October 2030</b>. There is no earlier new-tenancy-only date in the final policy summary.</li>
<li><b>Until then:</b> the existing minimum of <b>EPC E</b> continues for relevant PRS properties (<a href="{MEES_LANDLORD}" rel="nofollow">landlord guidance</a>; restated in the response).</li>
<li>Legislative steps (primary powers and secondary legislation) still need Parliamentary approval; the response aims for updated regulations coming into force around 2027, with compliance from 1 October 2030.</li></ul>
<p><span class="tag">UNVERIFIED</span> Exact band thresholds on the new EPC metrics will be confirmed once reformed EPCs and the Home Energy Model detail are finalised. This page does not invent those numbers.</p>
<h2 id="when-epc">3. When you may still need an EPC</h2>
<p>Official sources do <b>not</b> say "every holiday let must have EPC C". They say you must check.</p>
<ul class="tick"><li><b>England self-catering guidance:</b> "You must check whether you need an EPC" and links to EPC guidance for marketing, sale and let of dwellings (<a href="{SELF_CAT}" rel="nofollow">GOV.UK</a>).</li>
<li><b>EPC guidance (dwellings):</b> you must have an EPC when selling a property, renting out a property, or building a new property, and you must order one before marketing to sell or rent (<a href="{EPC_DWELL}" rel="nofollow">GOV.UK</a>).</li>
<li><b>Listed exceptions</b> on that same page include, among others: holiday accommodation rented out for less than 4 months a year; holiday accommodation let under a licence to occupy; and residential buildings intended to be used less than 4 months a year. Listed buildings can also be outside the rules in defined cases.</li>
<li>EPCs are normally valid for 10 years. You can <a href="{EPC_FIND}" rel="nofollow">find an energy certificate</a> on GOV.UK.</li>
<li><b>Licensing / sale:</b> selling a property is a clear case for an EPC. Some licensing applications (especially in Scotland) ask for an EPC — that is a local process requirement, not the England/Wales PRS MEES 2030 standard.</li></ul>
{CALLOUT(f'<p>If the official pages are vague for your exact letting pattern, follow <a href="{EPC_DWELL}" rel="nofollow">GOV.UK EPC guidance</a>, use <a href="{EPC_FIND}" rel="nofollow">find an energy certificate</a>, and ask your conveyancer, council licensing team or a qualified assessor. We do not invent a blanket holiday-let EPC grade.</p>',title='If your case is unclear')}
<p><span class="tag">UNVERIFIED</span> Whether a particular Airbnb-style booking model is always a "licence to occupy" vs a tenancy is a legal characterisation we do not decide here. Use the official exceptions list and professional advice for your facts.</p>
<h2 id="watch">4. What is under review / what hosts should watch</h2>
<ul class="tick"><li><b>Short-term lets in PRS MEES:</b> out of scope for now; under review; future SoS power and a tailored consultation before any decision (<a href="{MEES_RESP}" rel="nofollow">response</a>).</li>
<li><b>EPC regime reform:</b> new headline metrics on domestic EPCs confirmed in the partial response; launch of reformed domestic EPCs moved to the <b>second half of 2027</b> (<a href="{EPC_REFORM}" rel="nofollow">update 9 Mar 2026</a>).</li>
<li><b>PRS database / enforcement tools</b> for long-term PRS MEES (separate from short-term let registration) as described in the response and Renters\' Rights Act context.</li>
<li>Any update to the England self-catering "EPC where needed" wording.</li></ul>
<h2 id="scotland-ni">5. Scotland and Northern Ireland</h2>
<p>The higher MEES standard and short-term-let carve-out described above are <b>England and Wales</b> PRS policy.</p>
<ul class="tick"><li><b>Scotland:</b> has its own EPC and energy-efficiency framework. Short-term let licensing often requires an EPC for whole-house or flat lets — see <a href="scotland-short-term-let-licence-guide.html">Scotland short-term let licence guide</a>. <span class="tag">UNVERIFIED</span> for this page: detailed Scotland/NI MEES parity with the England/Wales 2030 PRS package.</li>
<li><b>Northern Ireland:</b> check Tourism NI / local official guidance; not covered in detail here.</li></ul>
<p>Check local rules rather than assuming England/Wales MEES applies unchanged.</p>
<h2 id="hosts">6. What hosts should do now</h2>
<ul class="tick"><li>If you only short-let in England or Wales: note that you are <b>not</b> in the 2030 PRS MEES duty for now, but watch the review.</li>
<li>Check whether you need a current EPC for sale, marketing, mortgage, insurance or a licence application using <a href="{EPC_DWELL}" rel="nofollow">GOV.UK</a> and <a href="{EPC_FIND}" rel="nofollow">find an energy certificate</a>.</li>
<li>If you also let long-term in the PRS: plan against the existing EPC E duty and the 1 October 2030 higher standard (<a href="{MEES_LANDLORD}" rel="nofollow">landlord guidance</a>; <a href="{MEES_RESP}" rel="nofollow">response</a>).</li>
<li>Keep fire, gas and electrical safety current — see <a href="holiday-let-fire-safety-england.html">England fire safety</a> and <a href="holiday-let-insurance-uk.html">holiday let insurance</a>.</li>
<li>Sign up below for an email when the short-let energy / MEES position changes.</li></ul>
{TOPICALERT('epc-energy-alert','epc-energy','Get an email when short-let energy or MEES rules change',
 f'We track the England and Wales PRS MEES short-term-let position and EPC reform against <a href="{MEES_RESP}" rel="nofollow">GOV.UK</a>. Short-term lets are out of PRS MEES for now but under review — we email you if that changes.',
 "Dates and sources we're watching",
 [f'<b>1 Oct 2030, England &amp; Wales PRS:</b> higher MEES compliance deadline for long-term private rented tenancies (<a href="{MEES_RESP}" rel="nofollow">source</a>)',
  f'<b>Second half of 2027:</b> reformed domestic EPCs launch target (<a href="{EPC_REFORM}" rel="nofollow">source</a>)'],
 [('','Choose your nation',False),('nation:england','England',False),('nation:wales','Wales',False)],
 'Your nation',
 'Pick England or Wales (where this MEES policy applies). You also get the weekly UK "what changed" email.',
 'We have no other short-let energy dates logged right now. If GOV.UK changes the short-let MEES position, we\'ll email you.')}
<h2 id="faq">Common questions</h2><div class="faq">{_efq}</div>
<p class="small">Related: <a href="england.html">England rules</a> · <a href="holiday-let-fire-safety-england.html">England fire safety</a> · <a href="holiday-let-insurance-uk.html">Holiday let insurance</a> · <a href="making-tax-digital-holiday-lets.html">Making Tax Digital</a> · <a href="holiday-let-tax-after-fhl-abolition.html">Holiday let tax after FHL</a> · <a href="deadlines.html">Deadlines</a> · <a href="guides.html">All guides</a>.</p>
<h2 id="sources">Official sources</h2>{SOURCES(_ES,'Show all official sources')}
<p class="small"><b>Not legal advice.</b> General information based on the GOV.UK sources above, checked {_CHECKED}. Marked UNVERIFIED where official pages leave detail open or where Scotland/NI rules were not re-verified for this page. Confirm with the linked guidance before acting. Free to cite with a link back. The UK Short-Let Rules team.</p>'''
page(f,t,b,desc=dsc,full_title='EPC and energy rules for holiday lets: MEES and when you need an EPC | UK Short-Let Rules',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{_eld}</script>',checked=_CHECKED)
