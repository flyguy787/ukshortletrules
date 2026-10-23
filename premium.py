# ---- Guide: England second homes council tax premium (from 1 Apr 2025) ----
PG='https://www.gov.uk/government/publications/long-term-empty-homes-and-second-homes-council-tax-premiums-and-exceptions/guidance-on-the-implementation-of-the-council-tax-premiums-on-long-term-empty-homes-and-second-homes'
PS=[('MHCLG: Guidance on the implementation of the council tax premiums on long-term empty homes and second homes (updated 1 May 2026, applies to England)',PG),
    ('GOV.UK: How Council Tax works, second homes and empty properties','https://www.gov.uk/council-tax/second-homes-and-empty-properties'),
    ('GOV.UK: Business rates for self-catering and holiday let accommodation',EN_BR)]
PEX=[('Class E','Home that would be someone\'s main home if they were not living in job-related armed forces accommodation'),
     ('Class F','Annex forming part of, or treated as part of, the main home'),
     ('Class G','Actively marketed for sale (up to 12 months)'),
     ('Class H','Actively marketed for let (up to 12 months)'),
     ('Class I','Unoccupied home where probate was recently granted (up to 12 months from the grant)'),
     ('Class J','Job-related home (second homes only)'),
     ('Class K','Occupied caravan pitch or boat mooring (second homes only)'),
     ('Class L','Seasonal home where year-round living is banned, use is limited to holiday accommodation, or a planning condition stops anyone staying more than 28 days in a row (second homes only)')]
PFAQ=[('What is the second homes council tax premium in England?','From 1 April 2025 councils in England can charge up to 100% extra council tax on second homes, so the bill can be up to double. For council tax, a second home is a property that is substantially furnished but is nobody\'s sole or main residence. Each council decides whether to charge it and at what rate.'),
      ('Does the premium apply to my holiday let?','It applies to a furnished holiday let that is still in the council tax system and is nobody\'s main home. If your holiday let is valued for business rates instead, because it was available for at least 140 nights and actually let for at least 70 nights in the last 12 months and you plan to offer it for 140 nights in the next 12, it pays business rates and the council tax premium does not apply.'),
      ('How much notice does a council have to give?','A council must make its first decision to charge a second homes premium at least one year before the start of the financial year it applies to. That is why most councils that charge it started on 1 April 2025.'),
      ('What are the exceptions?','The government has set mandatory exceptions that councils cannot switch off. For second homes they are Classes E to L, covering armed forces homes, annexes used as part of the main home, homes marketed for sale or let (12 months), recent probate (12 months), job-related homes, occupied caravan pitches and boat moorings, and seasonal or holiday-only homes restricted by planning.'),
      ('Can a council give a discount or extra exceptions?','Yes. Councils can add their own exceptions or offer discretionary reductions under section 13A of the Local Government Finance Act 1992. Ask your council what local policy it has.'),
      ('What if I think the premium has been charged wrongly?','Contact your council first, as it decides whether a home is a second home and whether an exception applies. If you are not happy with its answer, you may be able to appeal to the Valuation Tribunal.'),
      ('Does the "marketed for let" exception cover advertising as a holiday let?','The guidance says the sale and let exceptions are meant for owners genuinely trying to bring a home back into use as someone\'s main residence. We have not seen it say that holiday-let advertising counts, so check with your council before relying on it.')]
ec=''.join(f'<tr><td>{e(a)}</td><td>{e(b_)}</td></tr>' for a,b_ in PEX)
pfq=''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in PFAQ)
pld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in PFAQ]}).replace('</','<\\/')
pcl=''.join(f'<li><a href="councils/{slug(c)}.html">{e(c["name"])}</a>: {e(c["rule"])}</li>' for c in d['councils'] if c['nation']=='England' and c['verified'] and 'premium' in c['rule'])
f='england-second-homes-council-tax-premium.html'
t='England second homes council tax premium: holiday lets'
dsc='The second homes council tax premium in England from April 2025: who pays up to double council tax, when a holiday let pays business rates instead, the Class E to L exceptions, and council pages. Official sources.'
b=f'''<p class="lead">Since <b>1 April 2025</b>, councils in England can charge up to <b>100% extra council tax</b> on second homes, so the bill can be up to double. Here is when it hits a holiday let, when it does not, and the exceptions, with official sources.</p>
<div class="box"><p><b>Quick answer:</b> if your holiday let qualifies for <b>business rates</b> (140 nights available, 70 let), the council tax premium does not apply. If it is still on <b>council tax</b> and nobody lives there as their main home, your council may charge the premium unless an exception fits.</p></div>
<h2>Who it applies to</h2><ul>
<li>For council tax, a <b>second home</b> is a property that is substantially furnished but is nobody's sole or main residence.</li>
<li>Each council decides whether to charge the premium, at what rate (up to 100%), and whether in all or part of its area.</li>
<li>A council must make its first decision at least <b>one year</b> before the financial year it applies to.</li>
<li>Homes that are let out or lived in by someone as their main home are not second homes, even if the owner has several.</li></ul>
<h2>Holiday lets: council tax or business rates?</h2><p>{EN_BRT.strip()} Business rates are a separate tax, so check that the move is right for you. The Valuation Office Agency decides whether a property is assessed for business rates.</p>
<h2>Mandatory exceptions (from 1 April 2025)</h2><p>Councils cannot switch these off. They only remove the premium, not the normal council tax.</p>
<div class="tw"><table><tr><th>Class</th><th>Who it covers</th></tr>{ec}</table></div>
<p>Class M (major repairs, 12 months) applies to long-term empty homes only. Councils can also add their own exceptions or discounts under section 13A of the Local Government Finance Act 1992.</p>
<h2>What to check for your let</h2><ul>
<li>Is your let on council tax or business rates? Check your bill or the VOA listing.</li>
<li>Does your council charge the premium, and at what rate? See the council pages below or your council's website.</li>
<li>Does a planning condition limit the property to holiday use or stop stays over 28 days in a row? Class L may apply. Ask the council.</li>
<li>Is it an annex used as part of your main home? Class F may apply.</li>
<li>Does your council have a local exceptions or discount policy?</li></ul>
<h2>Council pages with premium details</h2><ul>{pcl}</ul><p><a href="england.html">All England rules</a> · <a href="councils.html">All councils</a></p>
<p>Wales has its own council tax premiums and a different 182-day business rates test. See <a href="wales.html">Wales rules</a>. For income tax, see <a href="holiday-let-tax-after-fhl-abolition.html">holiday let tax after the FHL abolition</a>.</p>
<div class="box"><h2>Get told when council tax rules for holiday lets change</h2><p>One short, sourced email a week.</p>{FORM}</div>
<h2>Common questions</h2>{pfq}
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in PS)}</ul>
<p class="small"><b>Not tax advice.</b> Checked {C}. Your council decides whether a premium or exception applies, so check with them before acting.</p>'''
page(f,t,b,desc=dsc,full_title='England second homes council tax premium for holiday lets (2025) | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{pld}</script>')
