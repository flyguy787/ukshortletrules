# ---- Guide: Wales second homes council tax premium (up to 300% from 1 Apr 2023). Sources checked 23 Oct 2026 ----
WG='https://www.gov.wales/council-tax-empty-and-second-homes-html'
WCONS='https://www.gov.wales/classification-self-catering-properties-local-tax-purposes'
WBR='https://www.gov.uk/guidance/apply-for-business-rates-for-a-self-catering-property-in-wales'
WPS=[('Welsh Government: Council Tax on empty and second homes, guidance for local authorities (last updated 9 Mar 2023)',WG),
     ('GOV.UK: Apply for business rates for a self-catering property in Wales',WBR),
     ('GOV.WALES consultation: Classification of self-catering properties for local tax purposes (closed 30 Oct 2026)',WCONS),
     ('GOV.WALES: Registering visitor accommodation (overview)','https://www.gov.wales/registering-visitor-accommodation-overview')]
WPEX=[('Class 1','Marketed for sale at a reasonable price, or an offer accepted (up to 1 year; only once until it sells)'),
      ('Class 2','Marketed for let at a reasonable rent, or an offer accepted (up to 1 year; again only after a tenancy of 6 months or more)'),
      ('Class 3','Annex forming part of, or treated as part of, the main home'),
      ('Class 4','Home that would be someone\'s main home if they were not living in armed forces accommodation'),
      ('Class 5','Occupied caravan pitch or boat mooring (second homes only)'),
      ('Class 6','A planning condition stops anyone staying 28 days in a row in a year, limits it to holiday use only, or stops it being anyone\'s main home (second homes only)'),
      ('Class 7','Job-related home (second homes only)')]
WPFAQ=[('What is the second homes council tax premium in Wales?','Welsh councils can charge extra council tax on second homes, meaning homes that are substantially furnished but nobody\'s sole or main home. Since 1 April 2023 the premium can be up to 300% on top of the standard charge, so a bill of up to four times normal. Each council decides whether to charge it and at what rate.'),
       ('Does it apply to my holiday let?','Only if the let is on council tax. Since 1 April 2023 a self-catering property in Wales pays business rates only if it is available to let for at least 252 nights and actually let for at least 182 nights. If it misses those thresholds it moves to council tax, and the council\'s second homes premium applies unless an exception fits.'),
       ('Which exceptions matter most for holiday lets?','Class 6 is the big one: it covers homes where a planning condition stops anyone staying 28 days in a row in a year, limits the home to holiday use only, or stops it being anyone\'s main home. Class 3 covers annexes used as part of your main home.'),
       ('Does advertising my holiday let count as "marketed for let"?','The guidance ties Class 2 to marketing at a reasonable rent compared with similar homes, with evidence such as a letting agency contract or Rent Smart Wales registration, which points to ordinary tenancies. We have not seen it say holiday-let advertising counts, so check with your council before relying on it.'),
       ('Can my council reduce the premium for my holiday let?','Yes, it can. Councils can choose which types of property the premium applies to, and section 13A of the Local Government Finance Act 1992 lets them reduce any bill. The Welsh Government encourages them to think about doing this for farm barn conversions, annexes or garage conversions that are part of the owner\'s home, and lodges, caravans or chalets that have moved to council tax. Ask your council for its policy.'),
       ('How much notice does a council have to give?','A council\'s first decision to charge a second homes premium must be made at least 1 year before the financial year it applies to. After that, it can change the rate before the start of each financial year, usually when full Council sets the budget.'),
       ('Is this the same as registering with the Welsh Revenue Authority?','No. The premium is council tax. Separately, Wales requires visitor accommodation providers to register with the Welsh Revenue Authority. It is free, and the deadline is 31 March 2027.')]
wec=''.join(f'<tr><td>{e(a)}</td><td>{e(b_)}</td></tr>' for a,b_ in WPEX)
wfq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in WPFAQ)
wld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in WPFAQ]}).replace('</','<\\/')
wcl=''.join(f'<li><a href="councils/{slug(c)}.html">{e(c["name"])}</a>: {e(c["rule"])}</li>' for c in d['councils'] if c['nation']=='Wales' and c['verified'] and 'premium' in c['rule'])
f='wales-second-homes-council-tax-premium.html'
t='Wales second homes council tax premium: holiday lets'
dsc='The Welsh second homes council tax premium (up to 300%): when a holiday let pays it after missing the 252/182-night business rates test, the Class 1 to 7 exceptions, and council rates. Official sources.'
b=f'''{TLDR(['<b>Up to 4 times normal council tax.</b> Since 1 April 2023, councils in Wales can charge a premium of up to 300% on second homes: furnished homes that are nobody\'s sole or main home.',
'<b>Business rates means no premium.</b> A Welsh holiday let stays on business rates only if it is available to let for at least 252 nights and actually let for at least 182 nights in 12 months. Miss that and it moves to council tax, where the premium can apply.',
'<b>Your council decides</b> whether to charge it, at what rate and on which types of property. Its first decision must be made at least 1 year before the financial year it applies to.',
'<b>Exceptions (Classes 1 to 7)</b> remove the premium. For holiday lets the big one is Class 6: a planning condition that limits the home to holiday use, stops stays of 28 days in a row, or stops it being anyone\'s main home. Councils can also reduce bills, for example for annexes or garage conversions that are part of your home.',
f'<b>The 182-night test is under review.</b> The Welsh Government <a href="{WCONS}" rel="nofollow">consulted</a> from 31 July to 30 October 2026 on the criteria for classing self-catering properties and on exemptions. The current 252/182 test still applies until any change is made.',
'<b>Do now:</b> check <a href="#premium-checklist">what to check for your let</a>, track your nights with the <a href="occupancy-threshold-tracker.html">occupancy tracker</a>, and <a href="#wales-alert">get an email when the rules change</a>.'],sub='From Welsh Government guidance, GOV.UK and GOV.WALES. Not tax advice.')}
<p class="lead">When the Welsh second homes premium hits a holiday let, the exceptions, and what each council we cover charges, with official sources.</p>
<h2>Who it applies to</h2><ul>
<li>For this premium, a <b>second home</b> is a home that is substantially furnished but is nobody's sole or main home.</li>
<li>Since 1 April 2017 Welsh councils have been able to charge up to 100%. From 1 April 2023 the maximum is <b>300%</b>.</li>
<li>Each council decides whether to charge it, at what rate, and which types of property it covers.</li>
<li>A council's first decision must be made at least <b>1 year</b> before the financial year it applies to. It can change the rate before each financial year starts.</li></ul>
<h2>Holiday lets: business rates or council tax?</h2><p>Since 1 April 2023 a self-catering property in Wales is valued for business rates only if it is available to let for at least <b>252 nights</b> and actually let for at least <b>182 nights</b> in the 12-month period you use. If it misses this, it moves to council tax and the second homes premium can apply. Track your nights with the <a href="occupancy-threshold-tracker.html">occupancy threshold tracker</a>.</p>
<h2>Exceptions (Council Tax (Exceptions to Higher Amounts) (Wales) Regulations 2015)</h2><p>Councils cannot charge the premium on these. They remove the premium, not the normal council tax.</p>
<div class="tw"><table><tr><th>Class</th><th>Who it covers</th></tr>{wec}</table></div>
<p>Councils can also reduce the premium or the whole bill under section 13A of the Local Government Finance Act 1992. The Welsh Government suggests they consider this for farm barn conversions, annexes or garage conversions that are part of the owner's home, and lodges, caravans or chalets that move to council tax.</p>
<h2 id="premium-checklist">What to check for your let</h2><ul>
<li>Did it meet 252 available and 182 let nights? If not, expect a move to council tax.</li>
<li>Does a planning condition limit it to holiday use or stop stays of 28 days in a row? Class 6 may apply. Ask the council and keep the planning decision notice.</li>
<li>Is it an annex or garage conversion used as part of your main home? Class 3 may apply, or the council may have a local reduction policy.</li>
<li>What rate does your council charge? See below or your council's website.</li></ul>
<h2>Council rates we track</h2><ul>{wcl}</ul><p><a href="wales.html">All Wales rules</a> · <a href="councils.html">All councils</a></p>
<p>England has a different premium (up to 100%) and a 140/70-night business rates test: see <a href="england-second-homes-council-tax-premium.html">England second homes council tax premium</a>. Holiday lets in Wales must also <a href="wales-registration-checker.html">register with the Welsh Revenue Authority</a> by 31 March 2027.</p>
{NATALERT('wales','wales-premium','We track the Welsh second homes council tax premium, the 252/182-night business rates test, council premium rates and other Welsh short-let rules against official sources, and email you when one changes.',nats=('Wales','England / Wales / NI'))}
<h2>Common questions</h2>{wfq}
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in WPS)}</ul>
<p class="small"><b>Not tax advice.</b> Checked {C}. Your council decides whether a premium, exception or reduction applies, so check with them before acting.</p>'''
page(f,t,b,desc=dsc,full_title='Wales second homes council tax premium for holiday lets (up to 300%) | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{wld}</script>')
