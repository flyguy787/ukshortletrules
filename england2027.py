# ---- Guide: England short-term lets, what is coming in 2027 (registration, C5/PD, Article 4, premiums, Overnight Visitor Levy) ----
# Official sources only. Council rows are built from the same CX/data.json text as the council pages (no new local facts).
f='england-short-term-let-rules-2027.html'
t='England short-term let rules: what changes in 2027'
GHL='https://www.gov.uk/guidance/letting-out-a-self-catering-holiday-home-in-england-rules-and-regulations'
GC5='https://www.gov.uk/government/consultations/introduction-of-a-use-class-for-short-term-lets-and-associated-permitted-development-rights'
GC5D=GC5+'/introduction-of-a-use-class-for-short-term-lets-and-associated-permitted-development-rights'
GWP='https://www.gov.uk/guidance/when-is-permission-required'
PGP='https://www.gov.uk/government/publications/long-term-empty-homes-and-second-homes-council-tax-premiums-and-exceptions/guidance-on-the-implementation-of-the-council-tax-premiums-on-long-term-empty-homes-and-second-homes'
_EN=sorted([c for c in d['councils'] if c['nation']=='England' and c['verified'] and slug(c) in CX],key=lambda c:c['name'].replace('City of ',''))
_TL=[('12 Apr to 7 Jun 2023','Government consults on a new C5 short-term let use class and new permitted development rights.',GC5),
     ('19 Feb 2024','Government confirms a mandatory national register for all of England and says it will introduce the C5 use class, permitted development rights, and flexibility to let your own main home for up to 90 nights a year.',EN_REG),
     ('1 Apr 2025','Councils can charge up to a 100% council tax premium on second homes (furnished, nobody\'s main home), if they decided at least a year before.',PGP),
     ('26 Nov 2025 to 18 Feb 2026','Government consults on an Overnight Visitor Levy.',EN_OVL),
     ('10 Sep 2026','Government announces that mayors and Foundation Strategic Authority leaders will get the power to bring in an Overnight Visitor Levy.',EN_OVL),
     ('2 Oct 2026','GOV.UK updates its guidance: the national registration scheme is now expected to begin in March 2027.',GHL),
     ('March 2027 (expected)','National short-term let registration scheme expected to begin. No regulations, portal or fee published yet.',GHL),
     ('Early 2028','Government expects mayors and Foundation Strategic Authority leaders to set out their visitor levy spending plans.',EN_OVL)]
_UP={'March 2027 (expected)','Early 2028'}  # not yet happened (as of the 28 Oct 2026 check)
_tl=VTL([(a,e(b),u,a in _UP) for a,b,u in _TL])
_ctrl=lambda c:CX[slug(c)]['ctrl'][0]
_noa4=[c for c in _EN if re.search(r'^No (short-let control area or )?Article 4 direction',_ctrl(c))]
_hmo=[c for c in _noa4 if re.search(r'Article 4[^.]*(HMO|multiple occupation)|(HMO|multiple occupation)[^.]*Article 4',_ctrl(c))]
_lk=lambda L:', '.join(f'<a href="councils/{slug(c)}.html">{e(c["name"])}</a>' for c in L)
_prem=[c for c in _EN if re.search(r'premium|double council tax',c['rule'])]  # Liverpool/Sefton rows say 'double council tax' (same 100% premium)
_prow=''.join(f'<tr><td><a href="councils/{slug(c)}.html">{e(c["name"])}</a></td><td>{e(c["rule"])}</td><td><time>{_fdate(max([C]+[ch["date"] for ch in CHG(c)]))}</time></td></tr>' for c in _prem)
EQ=[('When does the England short-term let register start?','GOV.UK says the mandatory national registration scheme for short-term lets in England is expected to begin in March 2027 (guidance updated 2 Oct 2026). No regulations, registration portal or fee have been published yet, so you cannot register today.'),
    ('Will the register apply to hotels and B&Bs?','No. The government said in February 2024 that the register and the planning changes are focused on short-term lets and will not affect hotels, hostels or B&Bs.'),
    ('Is the C5 use class law yet?','No. The government consulted on a C5 short-term let use class and permitted development rights in 2023 and said in February 2024 that it will introduce them, but no legislation has been made. Until then your local planning authority decides case by case whether letting a home is a material change of use. In Greater London the separate 90-night rule applies.'),
    ('Can my council use an Article 4 direction to stop holiday lets?','An Article 4 direction removes permitted development rights in an area. Under the 2023 proposals, a new permitted development right would let homes switch to short-term lets without an application, and areas would only see a change where a council removed that right with an Article 4 direction. Because that right does not exist yet, no English council can use one for short lets today. Existing Article 4 directions in the areas we track cover things like small HMOs and building alterations, not holiday-let use.'),
    ('Is there a tourist tax in England?','Not yet. On 10 Sep 2026 the government announced that mayors and Foundation Strategic Authority leaders will get the power to bring in an Overnight Visitor Levy, charged as a percentage of the accommodation cost. A bill is still to come, and no levy applies yet.')]
_eld=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in EQ]}).replace('</','<\\/')
_efq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in EQ)
_ES=[('GOV.UK: Letting out a self-catering holiday home in England (updated 2 Oct 2026)',GHL),
     ('DCMS: Delivering a registration scheme for short-term lets (19 Feb 2024)',EN_REG),
     ('MHCLG: Introduction of a use class for short-term lets and associated permitted development rights (consultation, 2023)',GC5),
     ('Planning Practice Guidance: When is permission required? (Article 4 directions)',GWP),
     ('MHCLG: Guidance on the council tax premiums on long-term empty homes and second homes',PGP),
     ('MHCLG: Local leaders handed powers to drive investment in communities (Overnight Visitor Levy, 10 Sep 2026)',EN_OVL),
     ('Liverpool City Region Combined Authority: New powers for Mayor to introduce overnight visitor levy (11 Sep 2026)',LCROVL)]
dsc='England short-term let changes for 2027: national register expected March 2027, the C5 use class and Article 4 directions, second homes premiums and the Overnight Visitor Levy. Official sources.'
b=f'''<p class="lead">England is catching up with Scotland and Wales. A national register for short-term lets is expected in March 2027, planning changes have been promised, councils already charge second homes premiums, and mayors are getting a visitor levy power. Here is where each one stands, with the official source for every fact.</p>
{TLDR([f'<b>Register:</b> a mandatory national registration scheme is <a href="{GHL}" rel="nofollow">expected to begin in March 2027</a> (GOV.UK, updated 2 Oct 2026). No regulations, portal or fee yet, so you cannot register today.',
 '<b>Planning:</b> the C5 short-term let use class is still only a proposal. Today your local planning authority decides whether letting a home is a material change of use (London: 90-night rule).',
 f'<b>Second homes:</b> since 1 Apr 2025 councils can charge up to a 100% council tax premium. {len(_prem)} of the {len(_EN)} English council areas we track charge one.',
 f'<b>Tourist tax:</b> the <a href="{EN_OVL}" rel="nofollow">Overnight Visitor Levy</a> was announced on 10 Sep 2026 but still needs a bill. No levy applies yet.',
 '<b>Do now:</b> check <a href="#premiums">your council</a>, ask your council how registration will work locally (as GOV.UK advises), and <a href="#england-alert">get an email</a> when any of this changes.'],
 title='In short: what changes in England in 2027')}
{SCARDS([('Registration','coming','Expected March 2027','National, mandatory, mainly online. No regulations, portal or fee yet.','register'),
 ('Planning use class (C5)','proposed','Proposal, not law','Promised in Feb 2024. No legislation made yet.','planning'),
 ('Second-home premiums','in',f'{len(_prem)} of {len(_EN)} tracked councils','Up to 100% extra (double bill) since 1 Apr 2025.','premiums'),
 ('Visitor levy','announced','Announced, not in force','Power for mayors announced 10 Sep 2026. Bill still to come.','levy')])}
{TOC([('timeline','Timeline'),('register','Registration'),('planning','Planning (C5)'),('article4','Article 4'),('premiums','Second homes premiums'),('levy','Visitor levy'),('england-alert','Get alerts'),('faq','Questions'),('sources','Sources')])}
<h2 id="timeline">Timeline</h2>{_tl}
<h2 id="register">1. The national registration scheme <span class="pill p-coming">Coming</span></h2>
<p>The Levelling-up and Regeneration Act 2023 gives the government the power to set up a register of short-term lets. In February 2024 the government chose (<a href="{EN_REG}" rel="nofollow">DCMS statement</a>):</p>
<ul class="tick"><li>A <b>mandatory, national scheme covering all of England</b> (61% of consultation responses supported this).</li>
<li>Designed to be "light touch, low cost and simple to use", delivered mainly online.</li>
<li>It would still consider a threshold so people who let their home only occasionally are not over-regulated.</li>
<li>The register will not affect hotels, hostels or B&amp;Bs.</li></ul>
<p><b>Status:</b> not in force. GOV.UK now says it is <b>expected to begin in March 2027</b> (updated 2 Oct 2026). Who runs it, how often you register, what information is needed and any fee have not been published.</p>
{CALLOUT(f'<p>You cannot register yet. Until the scheme opens, GOV.UK tells hosts to contact their council about how registration will work locally (<a href="{GHL}" rel="nofollow">GOV.UK</a>).</p>')}
<h2 id="planning">2. Planning: the C5 use class and permitted development <span class="pill p-proposed">Proposed</span></h2>
<p>In 2023 the government consulted on a new use class, <b>C5 Short Term Let</b>, defined as "use of a dwellinghouse that is not a sole or main residence for temporary sleeping accommodation for the purpose of holiday, leisure, recreation, business or other travel" (<a href="{GC5D}" rel="nofollow">consultation document</a>). Under the proposals:</p>
<ul class="tick"><li>Existing short lets meeting the definition would move into C5 automatically, without needing permission.</li>
<li>New permitted development rights would allow changes between homes (C3) and short lets (C5) without permission where short lets are not a local issue.</li></ul>
<p>In February 2024 the government said it will introduce the use class, the permitted development rights and flexibility for homeowners to let their own main home for up to 90 nights a year (<a href="{EN_REG}" rel="nofollow">DCMS</a>).</p>
<p><b>Status:</b> proposal only. No legislation has been made.</p>
{CALLOUT(f'<ul><li>Today your local planning authority decides whether letting a property is a material change of use (<a href="{GHL}" rel="nofollow">GOV.UK</a>).</li><li>In Greater London the 90-night rule applies (<a href="london-90-night-counter.html">count your nights</a>).</li><li>For the detail, see <a href="england-holiday-let-planning-permission.html">do I need planning permission for a holiday let?</a></li></ul>')}
<h2 id="article4">3. Article 4 directions</h2>
<p>An Article 4 direction lets a council remove permitted development rights in an area, so that change needs a planning application (<a href="{GWP}" rel="nofollow">Planning Practice Guidance</a>).</p>
<p>Under the 2023 proposals, a new permitted development right would let a home switch to a short let without an application, and areas would only see a change where a council removed that right with an Article 4 direction (<a href="{GC5D}" rel="nofollow">consultation document</a>). That right does not exist yet, so there is nothing for a council to remove for short lets today.</p>
<p class="stat"><b>{len(_noa4)} of {len(_EN)}</b> English council areas we track: council pages record a search that found no short-let control area or Article 4 direction aimed at holiday-let use.</p>
{CALLOUT(f'<p>Where those councils do have Article 4 directions, they mostly cover things like turning houses into small HMOs ({_lk(_hmo)}) or building alterations in conservation areas, not holiday lets. Each council page gives the search date and source.</p>',title='In the councils we track')}
<h2 id="premiums">4. Second homes council tax premiums <span class="pill p-in">In force</span></h2>
<ul class="tick"><li>Since 1 Apr 2025, councils in England can charge up to a <b>100% premium</b> on second homes (furnished, nobody's main home), so the bill can be up to double.</li>
<li>A council must decide at least a year before the financial year it starts.</li>
<li>Holiday lets valued for business rates do not pay it (<a href="{PGP}" rel="nofollow">MHCLG guidance</a>).</li></ul>
<p class="stat"><b>{len(_prem)} of {len(_EN)}</b> English council areas we track charge a second homes premium.</p>
{COLLAPSE(f'Show all {len(_prem)} councils', f'<div class="tw"><table class="stk"><tr><th>Council</th><th>What we track</th><th>Last checked</th></tr>{_prow}</table></div>', filt='Type your council, e.g. Cornwall')}
{CALLOUT('<p>If your home is a furnished second home that is nobody\'s main home and is not valued for business rates, your council can charge up to double. Find your council above. How it works and the exceptions: <a href="england-second-homes-council-tax-premium.html">England second homes premium guide</a>.</p>')}
<h2 id="levy">5. Overnight Visitor Levy (tourist tax) <span class="pill p-announced">Announced</span></h2>
<p>On 10 Sep 2026 the government announced that mayors and Foundation Strategic Authority leaders will get the power to introduce an Overnight Visitor Levy (<a href="{EN_OVL}" rel="nofollow">MHCLG</a>):</p>
<ul class="tick"><li>It must be charged as a <b>percentage of the accommodation cost</b>, not a flat fee.</li>
<li>Local leaders decide whether to use it and can offer exemptions (such as campsites).</li>
<li>Temporary accommodation, shelters and refuges would not be subject to it.</li>
<li>Hotels and other accommodation providers would pay it to the authority.</li>
<li>A bill will be introduced "in due course", and the government expects spending plans by early 2028.</li></ul>
<p>In the government's announcement, the mayors of London, the Liverpool City Region, the East Midlands, West Yorkshire, the West of England, South Yorkshire, and York and North Yorkshire welcomed the power; York and North Yorkshire said no decision will be made without a full public consultation. The Liverpool City Region Mayor says a levy could raise up to £18m a year there (<a href="{LCROVL}" rel="nofollow">LCRCA</a>).</p>
{CALLOUT('<p>No levy has been set anywhere in England yet. See <a href="councils/liverpool.html">Liverpool</a>, <a href="councils/sefton.html">Sefton</a> and the <a href="uk-visitor-levy-map.html">UK visitor levy map</a>.</p>')}
{NATALERT('england','england-2027','We track the England short-term let register, the C5 planning changes, council tax premiums and the Overnight Visitor Levy against official sources, and email you when one changes.',nats=('England','England / NI'))}
<h2 id="faq">Common questions</h2><div class="faq">{_efq}</div>
<h2 id="sources">Official sources</h2>{SOURCES(_ES,'Show all official sources')}
<p class="small"><b>Not legal advice.</b> General information based on the official sources above, checked 28 Oct 2026. Check with your council before acting. See also <a href="england.html">all England rules</a> and the <a href="changes.html">changes log</a>.</p>{FILTJS}'''
page(f,t,b,desc=dsc,full_title='England Short-Term Let Rules 2027: Register, C5 & Levy | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{_eld}</script>')
