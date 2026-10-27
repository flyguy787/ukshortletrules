# ---- Guide: England holiday let planning permission ----
GH='https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'
GC5='https://www.gov.uk/government/consultations/introduction-of-a-use-class-for-short-term-lets-and-associated-permitted-development-rights'
GWP='https://www.gov.uk/guidance/when-is-permission-required'
GLDC='https://www.gov.uk/guidance/lawful-development-certificates'
S55='https://www.legislation.gov.uk/ukpga/1990/8/section/55'
S171A='https://www.legislation.gov.uk/ukpga/1990/8/section/171A'
L115='https://www.legislation.gov.uk/ukpga/2023/55/section/115'
SI452='https://www.legislation.gov.uk/uksi/2024/452/made'
D44='https://www.legislation.gov.uk/ukpga/2015/20/section/44'
PS=[('GOV.UK: Letting out a self-catering holiday home in England',GH),
    ('GOV.UK: Use class for short-term lets consultation (2023)',GC5),
    ('Planning Practice Guidance: When is permission required?',GWP),
    ('Planning Practice Guidance: Lawful development certificates',GLDC),
    ('Town and Country Planning Act 1990, section 55: meaning of development',S55),
    ('Town and Country Planning Act 1990, section 171A: breach of planning control',S171A),
    ('Levelling-up and Regeneration Act 2023, section 115: enforcement time limits',L115),
    ('SI 2024/452: commencement and transitional provisions (regulation 5)',SI452),
    ('Deregulation Act 2015, section 44: London short-term use',D44)]
PQ=[('Do I need planning permission to holiday let my house in England?','Sometimes. There is no national rule that every holiday let needs planning permission. GOV.UK says your local planning authority decides, based on how the property is used for short-term letting and its impact on neighbours and the local area, and that you should contact your council to confirm. In Greater London there is a separate 90-night limit.'),
    ('Is there a C5 use class for short-term lets in England?','No. The government consulted on a new C5 use class for short-term lets, with new permitted development rights, from 12 April to 7 June 2023. GOV.UK still says it is analysing the feedback (checked 27 Oct 2026), so C5 is not law in England. Wales is different: it has had a short-term let use class since October 2022.'),
    ('What is the London 90-night rule?','In Greater London, using a home as temporary sleeping accommodation (stays under 90 nights) normally needs planning permission. The exception is that you do not need permission if the total nights let in a calendar year are 90 or fewer and the person providing the accommodation pays council tax on the home (Deregulation Act 2015, section 44).'),
    ('Do I need planning permission to holiday let a garage, annexe or outbuilding?','Often this is where hosts get caught out. Converting a building is usually building work, and building operations count as development under section 55 of the Town and Country Planning Act 1990. If an existing permission has a condition, for example that an annexe is only used alongside the main house or that a building is for holiday use only, not following it is a breach of planning control. Ask your council before you convert or let one separately.'),
    ('How can I get certainty that I do not need planning permission?','You can apply to your council for a lawful development certificate. One for a proposed use (section 192) confirms a planned use would be lawful; one for an existing use (section 191) confirms a use already happening is lawful. Planning merits are not considered, only the facts and the law. Many councils also offer pre-application advice, and some charge for it.'),
    ('What happens if I let without planning permission I needed?','The council can take enforcement action. In England the time limit for enforcement is now 10 years for breaches that happen on or after 25 April 2024 (Levelling-up and Regeneration Act 2023, section 115). Breaches that happened before that date keep the old time limits.'),
    ('Can councils use Article 4 directions to stop holiday lets in England?','An Article 4 direction removes permitted development rights. Under the 2023 proposals, councils would have been able to remove new rights to change a home into a short-term let where there is local concern. Those rights do not exist yet, so for now councils rely on deciding case by case whether a letting is a material change of use, and on Local Plan policies.'),
    ('Do restrictive covenants or my lease matter for planning?','They are not a planning matter, so planning permission does not override them. Planning guidance says land ownership restrictions such as deeds or covenants should be checked with a legal professional. Check your lease, deeds and mortgage terms separately.'),
    ('If I have planning permission, do I need anything else?','Yes, usually. Planning permission or a lawful development certificate does not remove the need for Building Regulations approval or other consents. Holiday lets also have fire, gas and electrical safety duties, and a national short-term let registration scheme is expected to start in March 2027 (GOV.UK).')]
_pf=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in PQ)
_pld='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in PQ]}).replace('</','<\\/')+'</script>'
_enc=sorted([c for c in d['councils'] if c['nation']=='England' and c['verified']],key=lambda c:c['name'].replace('City of ',''))
_cl=''.join(f'<li><a href="councils/{slug(c)}.html">{e(c["name"])}</a></li>' for c in _enc)
f='england-holiday-let-planning-permission.html'
t='Do I need planning permission for a holiday let in England?'
dsc='When does an English holiday let need planning permission? Material change of use, London 90 nights, annexes, C5 status, certificates and enforcement.'
b=ANSWER(t,f'Sometimes. There is no national rule in England that every holiday let needs planning permission. <a href="{GH}" rel="nofollow">GOV.UK</a> says your local planning authority decides, based on how the property is used for short-term letting and its impact on neighbours and the local area. In Greater London, letting a whole home for more than <a href="london-90-night-counter.html">90 nights a calendar year</a> needs permission. Building work, and breaking a condition on an existing permission, are separate triggers.')+TOP_PICK(next(n for n in d['nations'] if n['id']=='england'))+f'''
<h2>The 4 questions that decide it</h2><ol>
<li><b>Is it a material change of use?</b> Planning permission is needed for &ldquo;development&rdquo;, which includes <a href="{S55}" rel="nofollow">material changes of use</a> of land and buildings. Whether letting a home to holidaymakers is one is decided by your council case by case. GOV.UK says it looks at how the property is used for short-term letting and its impact on neighbours and the local area.</li>
<li><b>Is it in Greater London?</b> Letting a whole home short term for more than 90 nights in a calendar year needs permission (<a href="{D44}" rel="nofollow">Deregulation Act 2015, s44</a>). Use our <a href="london-90-night-counter.html">90-night counter</a>.</li>
<li><b>Are you building or converting?</b> Building operations are development in their own right. Converting a garage, barn or outbuilding into a let usually involves them. Annexe and outbuilding lets are also where the next question bites.</li>
<li><b>Is there a planning condition?</b> Not following a condition on an existing permission is a <a href="{S171A}" rel="nofollow">breach of planning control</a>. Common examples are an annexe that may only be used alongside the main house, or a holiday-only occupancy condition. Check the planning history on your council&rsquo;s planning search.</li></ol>
<div class="box"><p><b>C5 is still only a proposal.</b> The government <a href="{GC5}" rel="nofollow">consulted</a> on a new C5 short-term let use class and new permitted development rights from 12 April to 7 June 2023. GOV.UK still says it is analysing the feedback (checked 27 Oct 2026). Until anything changes, the case-by-case test above applies. <a href="wales.html">Wales</a> already has a short-term let use class, and <a href="scotland.html">Scotland</a> has short-term let control areas.</p></div>
<h2>Getting certainty before you let</h2><ul>
<li><b>Lawful development certificate.</b> You can ask your council to confirm that a <a href="{GLDC}" rel="nofollow">proposed use (s192) or an existing use (s191)</a> is lawful. The council looks only at the facts and the law, not planning merits. You need to describe exactly what you plan to do and send evidence, plus the fee.</li>
<li><b>Pre-application advice.</b> Planning guidance says your council should be the <a href="{GWP}" rel="nofollow">first point of contact</a>, and some councils charge for pre-application advice.</li>
<li><b>Planning application.</b> If permission is needed, apply to your council. If you are refused, you can appeal to the Planning Inspectorate.</li></ul>
<h2>If you let without permission you needed</h2>
<p>The council can take enforcement action. In England the time limit is now <b>10 years</b> for breaches on or after 25 April 2024 (<a href="{L115}" rel="nofollow">LURA 2023, s115</a>). Breaches that happened before that date keep the old limits (<a href="{SI452}" rel="nofollow">SI 2024/452, reg 5</a>). That means a let that has run for a few years is not automatically safe.</p>
<h2>Local planning policies we track</h2><ul>
<li><a href="councils/isles-of-scilly.html">Isles of Scilly</a>: the adopted Local Plan restricts holiday-let conversions and needs principal residence on new homes.</li>
<li><a href="councils/derbyshire-dales.html">Derbyshire Dales and the Peak District</a>: the National Park&rsquo;s holiday-occupancy policy, and a draft principal residence clause (not adopted).</li>
<li><a href="councils/new-forest.html">New Forest</a>: draft National Park Local Plan proposes principal residence conditions on new homes (not adopted).</li>
<li><a href="councils/city-of-york.html">City of York</a>: draft short-term holiday lets planning guidance (not yet in force).</li>
<li><a href="councils/bournemouth-christchurch-and-poole.html">Bournemouth, Christchurch and Poole</a>: May 2026 motion to gather evidence on short lets and Article 4.</li>
<li><a href="councils/west-devon.html">West Devon</a> and <a href="councils/teignbridge.html">Teignbridge</a>: Dartmoor National Park holiday-let conditions.</li></ul>
<h2>Your council</h2><p>Every English council page has the local planning position, council tax and levy news, with sources:</p><ul>{_cl}</ul>
<h2>Common questions</h2>{_pf}
<p>Related: <a href="holiday-let-fire-safety-england.html">Holiday let fire safety in England</a> · <a href="england-second-homes-council-tax-premium.html">Second homes council tax premium</a> · <a href="occupancy-threshold-tracker.html">Business rates or council tax tracker</a> · <a href="holiday-let-tax-after-fhl-abolition.html">Holiday let tax after FHL</a> · <a href="buyer-due-diligence-checker.html">Buying a holiday let? Due-diligence checker</a></p>
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in PS)}</ul>
<p class="small"><b>Not legal or planning advice.</b> Checked 27 Oct 2026. Planning decisions depend on the facts of each property, so ask your council or a planning professional before acting.</p>'''
page(f,'Holiday let planning permission in England',b,desc=dsc,full_title='Do I Need Planning Permission for a Holiday Let? (England 2026)',head=OGT(f,t,dsc)+_pld,noh1=False)
