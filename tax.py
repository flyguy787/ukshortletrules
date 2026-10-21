# ---- Guide: holiday let tax after FHL abolition (UK-wide) ----
TS=[('HMRC policy paper: Abolition of the furnished holiday lettings tax regime (updated 7 Nov 2024)','https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/abolition-of-the-furnished-holiday-lettings-tax-regime'),
    ('HMRC Capital Gains Manual CG73505: FHL, consequences of abolition','https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg73505'),
    ('Finance Act 2025, Schedule 5','https://www.legislation.gov.uk/ukpga/2025/8/schedule/5'),
    ('GOV.UK: Work out your rental income when you let property (updated 19 Mar 2025)','https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income'),
    ('GOV.UK: Tax-free allowances on property and trading income','https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income')]
TROWS=[('Mortgage and loan interest (individuals)','Deducted in full from profits','Restricted: relief only at the basic rate of Income Tax, as for other residential landlords'),
    ('Furniture, equipment and fittings','Capital allowances on new spending','Replacement of domestic items relief for replacing items. An existing capital allowances pool can still be written down'),
    ('Losses','Kept in a separate FHL pot','Carried forward and set against your UK (or overseas) property business profits'),
    ('Capital Gains Tax reliefs on sale','Business Asset Disposal Relief, rollover relief, gift relief could apply','No longer available for disposals from 6 Apr 2025, apart from limited transitional cases'),
    ('Pension contributions','Profits counted as relevant UK earnings','No longer counted as relevant UK earnings'),
    ('Tax return','Separate FHL pages','Reported as part of your ordinary property business')]
TFAQ=[('When was the furnished holiday let tax regime abolished?','From 6 April 2025 for Income Tax and Capital Gains Tax, and from 1 April 2025 for Corporation Tax. It applies across the whole UK.'),
      ('How is holiday let income taxed now?','Income and gains from a former furnished holiday let form part of your UK (or overseas) property business and are taxed in the same way as other property income and gains.'),
      ('Can I still deduct my mortgage interest?','If you let as an individual, finance costs such as mortgage interest are now restricted: you get relief at the basic rate of Income Tax only, the same as other residential landlords. HMRC says UK and non-UK resident companies are not affected by this restriction.'),
      ('What happens to capital allowances I already claimed?','If you have an existing capital allowances pool, you can keep claiming writing-down allowances on it. New spending on or after the change is dealt with under the normal property rules, which includes replacement of domestic items relief.'),
      ('What happens to my old FHL losses?','Losses carried forward from your FHL business can be set against future profits of your UK (or overseas) property business.'),
      ('Can I still get Business Asset Disposal Relief when I sell?','Not for disposals of a holiday let business on or after 6 April 2025. It may still be available in limited cases, for example where an FHL business actually stopped before 6 April 2025 and assets are sold within the normal 3-year period.'),
      ('Is there a tax-free allowance for small amounts of rental income?','Yes. Individuals can use a property allowance of up to £1,000 a tax year. If your gross property income is £1,000 or less you do not need to tell HMRC. Above that you can deduct the £1,000 allowance instead of your actual expenses.'),
      ('Do the 105-night and 210-day tests still matter?','Not for Income Tax or Capital Gains Tax. Those tests decided whether a property counted as a furnished holiday let, which no longer exists. Separate night-count rules still apply to business rates in Scotland and Wales.')]
tr=''.join(f'<tr><td>{e(a)}</td><td>{e(b_)}</td><td>{e(c)}</td></tr>' for a,b_,c in TROWS)
fq=''.join(f'<h3>{e(q)}</h3><p>{e(a)}</p>' for q,a in TFAQ)
ld=_j.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in TFAQ]}).replace('</','<\\/')
f='holiday-let-tax-after-fhl-abolition.html'
t='Holiday let tax after the FHL abolition'
dsc='How UK holiday lets are taxed since the furnished holiday let (FHL) regime ended in April 2025: mortgage interest, capital allowances, losses, CGT reliefs and pensions, with HMRC sources.'
b=f'''<p class="lead">The special tax treatment for <b>furnished holiday lets (FHLs)</b> ended in April 2025 across the whole UK. Holiday let income is now taxed like any other property income. Here is what changed, in plain English, with HMRC sources.</p>
<div class="box"><p><b>Dates:</b> from <b>6 April 2025</b> for Income Tax and Capital Gains Tax, and from <b>1 April 2025</b> for Corporation Tax. An anti-forestalling rule applies from 6 March 2024.</p></div>
<h2>Before and after</h2>
<div class="tw"><table><tr><th>Area</th><th>Under the FHL rules</th><th>Now</th></tr>{tr}</table></div>
<h2>What to check for your own lets</h2><ul>
<li><b>Mortgage interest:</b> if you own the let personally and pay higher-rate tax, your tax bill on the same profit may go up because interest relief is now limited to the basic rate.</li>
<li><b>Capital allowances pool:</b> keep claiming writing-down allowances on any existing pool. Treat new furniture and kit under the property rules.</li>
<li><b>Losses:</b> any FHL losses brought forward can now be used against profits from your other UK lets.</li>
<li><b>Selling soon:</b> FHL capital gains reliefs no longer apply to disposals from 6 April 2025, apart from narrow transitional cases. Take advice before selling.</li>
<li><b>Pensions:</b> holiday let profits no longer count as earnings for pension tax relief.</li>
<li><b>Small income:</b> if your gross property income is £1,000 or less a tax year, the property allowance means you may not need to tell HMRC.</li></ul>
<p>Local taxes are separate and did not change with the FHL abolition. See <a href="scotland-business-rates-checker.html">Scotland business rates or council tax</a>, <a href="wales.html">Wales rules</a> and the <a href="uk-visitor-levy-map.html">UK visitor levy map</a>.</p>
<div class="box"><h2>Get told when holiday let tax rules change</h2><p>One short, sourced email a week.</p>{FORM}</div>
<h2>Common questions</h2>{fq}
<h2>Official sources</h2><ul>{"".join(f'<li><a href="{u}" rel="nofollow">{e(n)}</a></li>' for n,u in TS)}</ul>
<p class="small"><b>Not tax advice.</b> Checked {C}. Tax depends on your circumstances, so speak to an accountant or HMRC before acting.</p>'''
page(f,t,b,desc=dsc,full_title='Holiday let tax after FHL abolition (April 2025) | UK Short-Let Rules Tracker',head=OGT(f,t,dsc)+f'<script type="application/ld+json">{ld}</script>')
