# ---- Guide: England Visitor Levy Bill explainer (introduced 4 Nov 2026) ----
# Official UK government and Parliament sources only. Anything uncertain marked UNVERIFIED.
f='england-visitor-levy-bill.html'
t='England Visitor Levy Bill: what hosts need to know'
EN_BILL='https://bills.parliament.uk/bills/4320'
EN_OVL_RESP='https://www.gov.uk/government/consultations/overnight-visitor-levy-in-england'
EN_OVL_PDF='https://assets.publishing.service.gov.uk/media/6aa2980c5f6e942efe37f0c9/Visitor_Levy_in_England_-_government_response.pdf'
_CHECKED='6 Nov 2026'
_TL=[('26 Nov 2025 to 18 Feb 2026','Government consults on an Overnight Visitor Levy in England.',EN_OVL_RESP),
     ('10 Sep 2026','Government publishes its response and announces that mayors and Foundation Strategic Authority leaders will get the power to bring in an Overnight Visitor Levy.',EN_OVL_ANN),
     ('4 Nov 2026','Government introduces the Visitor Levy (England) Bill in the House of Commons (Bill 177, 2026-27).',EN_OVL),
     ('Still to pass Parliament','The Bill is not yet law. No rate or start date applies anywhere in England under it.',EN_BILL),
     ('Early 2028 (expected)','Government expects mayors and Foundation Strategic Authority leaders to set out visitor levy spending plans once powers are in use.',EN_OVL)]
_UP={'Still to pass Parliament','Early 2028 (expected)'}
_tl=VTL([(a,e(b),u,a in _UP) for a,b,u in _TL])
EQ=[('Is there a tourist tax in England yet?','Not yet under this Bill. On 4 November 2026 the government introduced the Visitor Levy (England) Bill in the House of Commons. It still has to pass Parliament, and each strategic authority then decides whether to use the power after local consultation. No levy applies anywhere in England under the Bill today.'),
    ('Who would pay and who would account for the levy?','Hotels and other accommodation providers will be responsible for accounting for and paying the levy to the strategic authority. The government will give providers guidance on how to register, pay and report. As part of continuing technical engagement, the government is also considering whether booking platforms may help with collection and remittance on behalf of providers; that would not shift the legal duty away from the provider.'),
    ('Would it be a flat fee or a percentage?','A percentage of the accommodation cost, not a flat fee, so lower-cost stays pay less. Ten mayors have said any levy in their areas would be no higher than 5%. That is a mayoral commitment, not a statutory national cap in the Bill announcement.'),
    ('How long of a stay would be charged?','The levy would only apply to the first 28 consecutive days of a stay. Longer stays count as long-term accommodation.'),
    ('Who is exempt?','National exemptions confirmed for student accommodation, care homes, children\'s homes and school boarding houses. Temporary accommodation, shelters and refuges would not be charged. Mayors and local leaders can add limited local exemptions, for example camping pitches. Occasional hosts who only rent a spare room from time to time would only pay if they earn above a set amount, which local leaders can adjust.'),
    ('What must a mayor do before introducing a levy?','Publish a draft plan and an impact assessment (expected impact, proposed rate, threshold, exemptions and how the money will be spent), consult local people and businesses, seek the necessary agreement within the Strategic Authority, consider the responses, then publish the responses and final documents. In Foundation Strategic Authorities a levy can only go ahead with unanimous support. Authorities with a levy must publish an annual report on what they raise, spend and plan to spend.'),
    ('Does this affect short-term lets and holiday lets?','Yes in principle: hotels and other accommodation providers are in scope. Exact coverage of short-term lets in each area will be set locally in each scheme\'s plan after consultation. No scheme exists yet under the Bill.'),
    ('Where can I see every UK levy deadline in one place?','See our UK levy and licence deadline table, the UK visitor levy map and the England short-term let rules 2027 guide. Sign up below for England levy alerts.')]
_eld=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in EQ]}).replace('</','<\\/')
_efq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in EQ)
_ES=[('MHCLG: New visitor levy powers to put money back into local communities (Visitor Levy Bill, 4 Nov 2026)',EN_OVL),
     ('UK Parliament: Visitor Levy (England) Bill (Bill 177 2026-27, as introduced)',EN_BILL),
     ('MHCLG: Local leaders handed powers to drive investment in communities (Overnight Visitor Levy, 10 Sep 2026)',EN_OVL_ANN),
     ('MHCLG: Overnight visitor levy in England — consultation outcome and government response',EN_OVL_RESP),
     ('MHCLG: Visitor levy in England — government response (PDF)',EN_OVL_PDF),
     ('Liverpool City Region Combined Authority: New powers for Mayor to introduce overnight visitor levy (11 Sep 2026)',LCROVL)]
dsc='England Visitor Levy Bill (introduced 4 Nov 2026): who pays, how the percentage levy would work, exemptions, consultation rules and what is still UNVERIFIED. Official sources.'
b=f'''<p class="lead">On 4 November 2026 the government introduced the Visitor Levy (England) Bill in the House of Commons. It would let mayors and Foundation Strategic Authority leaders charge a percentage levy on overnight stays after local consultation. It is not yet law. Here is what the official sources say for hosts, agents and journalists.</p>
{TLDR([f'<b>Status:</b> Bill introduced 4 Nov 2026 (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>; <a href="{EN_BILL}" rel="nofollow">Parliament</a>). Not yet law. No levy applies anywhere in England under it.',
 f'<b>Who accounts and pays:</b> hotels and other accommodation providers will be responsible for accounting for and paying any levy. Government is still considering how platforms might help with collection (<a href="{EN_OVL}" rel="nofollow">UK gov, 4 Nov</a>; <a href="{EN_OVL_RESP}" rel="nofollow">government response</a>).',
 '<b>Design:</b> percentage of the accommodation cost (not a flat fee); first 28 consecutive nights only; local consultation and a draft plan required first.',
 '<b>Do now:</b> nothing to pay yet. Check whether your mayor has said they will consult, and <a href="#england-levy-alert">get an email</a> when England levy rules change.'],
 title='In short: the England Visitor Levy Bill')}
{SCARDS([('Bill status','announced','Introduced, not in force','Commons introduction 4 Nov 2026. Still to pass Parliament.','status'),
 ('Who is liable','announced','Accommodation providers','Providers account for and pay the levy to the authority.','liable'),
 ('Rate shape','announced','Percentage of stay cost','Not a flat fee. Ten mayors say any local levy would be no higher than 5%.','rate'),
 ('Start anywhere?','proposed','None yet','No rate or start date applies in England under the Bill today.','start')])}
{TOC([('timeline','Timeline'),('status','What the Bill is'),('liable','Who accounts and pays'),('design','How the levy would work'),('process','Before a scheme can start'),('exemptions','Exemptions'),('hosts','What hosts should do now'),('england-levy-alert','Get England levy alerts'),('faq','Questions'),('sources','Sources')])}
<h2 id="timeline">Timeline</h2>{_tl}
<h2 id="status">1. What the Bill is <span class="pill p-announced">Bill introduced</span></h2>
<p>The Visitor Levy (England) Bill is a government Bill sponsored by the Ministry of Housing, Communities and Local Government. Its long title is to make provision for and in connection with the imposition, by strategic authorities, of a new local tax in respect of stays in residential accommodation (<a href="{EN_BILL}" rel="nofollow">UK Parliament</a>). The Bill as introduced is Bill 177 2026-27.</p>
<p>On 4 Nov 2026 MHCLG said the Bill lets mayors and leaders who know their areas introduce a small fee on overnight stays, with money raised staying in the local area (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>). It builds on the 10 Sep 2026 announcement (<a href="{EN_OVL_ANN}" rel="nofollow">MHCLG</a>).</p>
{CALLOUT('<p>No levy has been set anywhere in England under this Bill. It still has to pass Parliament, and each strategic authority then decides whether to use the power. See the <a href="uk-levy-and-licence-deadlines.html">levy and licence deadline table</a> and the <a href="uk-visitor-levy-map.html">UK visitor levy map</a>.</p>')}
<h2 id="liable">2. Who accounts for and pays the levy</h2>
<p>This is the fact that matters most for hosts and agents:</p>
<ul class="tick"><li><b>Accommodation providers are responsible for accounting for and paying the levy</b> to the strategic authority. The government will give them guidance on how to register, pay and report (<a href="{EN_OVL}" rel="nofollow">MHCLG, 4 Nov 2026</a>).</li>
<li>Strategic authorities will help providers get it right. Enforcement powers are described as standard tax powers, in line with national self-assessed taxes, used proportionately by local leaders (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li>In the government response to the earlier consultation, the government said it maintains that the accommodation provider should be the party liable and must self-assess liability (<a href="{EN_OVL_RESP}" rel="nofollow">government response</a>).</li>
<li>As part of continuing technical engagement, the government <b>will also consider whether booking platforms may be able to take a role in supporting the collection and remittance of the levy</b> on behalf of the accommodation provider, to reduce burdens through economies of scale (<a href="{EN_OVL_RESP}" rel="nofollow">government response, para 6.3.6</a>). That consideration does not move the legal duty off the provider.</li></ul>
{CALLOUT(f'<p><b>Key fact (UK gov, 4 Nov 2026 and government response):</b> accommodation providers will be responsible for accounting for and paying any levy. Government is still considering how platforms might help with collection. Source: <a href="{EN_OVL}" rel="nofollow">MHCLG news, 4 Nov 2026</a>; <a href="{EN_OVL_RESP}" rel="nofollow">Overnight visitor levy consultation outcome</a>.</p>',title='For agents and hosts')}
<h2 id="design">3. How the levy would work</h2>
<ul class="tick"><li>Charged as a <b>percentage of the accommodation cost</b>, not a flat fee, so lower-cost stays pay less (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li>Ten mayors have committed that any levy in their areas would be <b>no higher than 5%</b> (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>). That is a mayoral commitment reported by government, not quoted here as a statutory national cap.</li>
<li>Applies only to the <b>first 28 consecutive days</b> of a stay; longer stays count as long-term accommodation (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li>Occasional hosts (for example people who only rent out a spare room from time to time) would only pay if they earn above a set amount; local leaders can adjust that threshold (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li>Money raised stays in the local area for things such as transport, high streets, public spaces, events and attractions (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li></ul>
<p><span class="tag">UNVERIFIED</span> Exact rates, start dates, accounting periods, software requirements and how short-term lets will be listed in each local plan are not set in the 4 Nov announcement. They will be decided locally after consultation, if and when the Bill becomes law.</p>
<h2 id="process">4. Before a scheme can start</h2>
<p>Those wanting to introduce a levy must (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>):</p>
<ul class="tick"><li>Publish a <b>draft plan and an impact assessment</b> covering expected impact on the local economy, businesses and visitors, plus the proposed rate, threshold, exemptions and how the money will be spent.</li>
<li><b>Consult</b> local people and businesses, seek the necessary agreement within the Strategic Authority, consider the views, publish the responses and issue final versions of both documents.</li>
<li>In <b>Foundation Strategic Authorities</b>, a levy can only go ahead with <b>unanimous support</b>.</li>
<li>Publish an <b>annual report</b> on what they raise, what they spend and future spending plans.</li></ul>
<p>The government still expects spending plans by early 2028 once powers are in use (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</p>
<h2 id="exemptions">5. Exemptions</h2>
<ul class="tick"><li>National exemptions confirmed for <b>student accommodation, care homes, children's homes and school boarding houses</b> (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li><b>Temporary accommodation, shelters and refuges</b> will not be charged (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li>
<li>Mayors and local leaders can set additional limited local exemptions, for example camping pitches (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>).</li></ul>
<h2 id="hosts">6. What hosts and agents should do now</h2>
<ul class="tick"><li>Nothing to register or pay under this Bill today: it is not law and no English scheme has started under it.</li>
<li>Watch your combined authority or mayor for any draft plan or consultation.</li>
<li>Keep the England short-term let register in view separately: GOV.UK still expects that register in March 2027 (<a href="england-short-term-let-rules-2027.html">England 2027 guide</a>).</li>
<li>Compare Scotland and Wales schemes on the <a href="uk-levy-and-licence-deadlines.html">deadline table</a> and <a href="uk-visitor-levy-map.html">levy map</a>.</li>
<li>Sign up below for England levy alerts when official sources change.</li></ul>
{NATALERT('england','england-levy-bill','We track the England Visitor Levy Bill, local mayoral consultations and any scheme that follows against official sources, and email you when one changes.',aid='england-levy-alert',nats=('England','England / Wales / NI'))}
<h2 id="faq">Common questions</h2><div class="faq">{_efq}</div>
<h2 id="sources">Official sources</h2>{SOURCES(_ES,'Show all official sources')}
<p class="small"><b>Not legal advice.</b> General information based on the official UK government and Parliament sources above, checked {_CHECKED}. Marked UNVERIFIED where the Bill announcement leaves detail to later guidance or local schemes. Check with your strategic authority before acting. See also <a href="england-short-term-let-rules-2027.html">England short-term let rules 2027</a>, <a href="uk-levy-and-licence-deadlines.html">levy and licence deadlines</a>, <a href="uk-visitor-levy-map.html">the levy map</a> and the <a href="changes.html">changes log</a>. Free to cite with a link back. The UK Short-Let Rules team.</p>'''
page(f,t,b,desc=dsc,full_title='England Visitor Levy Bill: who pays, rates and status | UK Short-Let Rules',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{_eld}</script>',checked=_CHECKED)
