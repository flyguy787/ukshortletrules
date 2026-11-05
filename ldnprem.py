# ---- Citable table: London second homes council tax premium by borough (5 Nov 2026) ----
# One row per London billing authority (32 boroughs + City of London). Sources checked 5 Nov 2026:
#  - MHCLG Council Taxbase 2025, local authority data (Second Homes Data: Table 6.06 premium applied in 2025-26, 6.11 homes charged a premium,
#    6.12 homes not charged because of an exception; as reported by councils in Oct 2025; revised 21 Jan 2026).
#  - MHCLG Council Tax levels 2026-27, Table 9 (average area Band D for two adults, incl. GLA, adult social care and parish precepts; 25 Mar 2026).
#  - The 3 councils that started on 1 Apr 2026 from their own pages / decisions: LBBD and RBKC council tax pages (100%), Hillingdon Full Council 22 Jan 2026 (100%).
# A 100% premium doubles the bill, so 'Band D on a second home' = 2 x average area Band D. Not re-checked borough by borough for 2026-27 (see note on page).
LPF='london-second-homes-council-tax-premium.html';LPCSV='london-second-homes-council-tax-premium-by-borough.csv'
LP_CTB='https://www.gov.uk/government/statistics/council-taxbase-2025-in-england'
LP_CTBX='https://assets.publishing.service.gov.uk/media/696f605ff6aa424b452e3359/2025_Local_Authority_Drop_Down.xlsx'
LP_CTL='https://www.gov.uk/government/statistics/council-tax-levels-set-by-local-authorities-in-england-2026-to-2027'
LP_LBBD='https://www.lbbd.gov.uk/council-tax/empty-properties-and-second-homes'
LP_RBKC='https://www.rbkc.gov.uk/council-tax/discounts-reductions-and-exemptions/council-tax-empty-properties'
LP_HILL='https://pre.hillingdon.gov.uk/council-tax/how-much-is-my-council-tax/2'
LP_WCAB='https://westminster.moderngov.co.uk/documents/s70431/Cabinet%20Report%20-%20Council%20Tax%20Discounts%20and%20Base.pdf'
LP_CAM='https://www.camden.gov.uk/council-tax-guide'
LP_TH='https://www.towerhamlets.gov.uk/lgnl/council_and_democracy/council_tax/Second-homes-and-empty-properties/Second-homes-premium.aspx'
LP_HILLM='https://modgov.hillingdon.gov.uk/documents/g4968/Public%20minutes%2022nd-Jan-2026%2019.30%20Council.pdf?T=11'
# (name, premium applied 2025-26 per MHCLG, homes charged a premium Oct 2025, homes not charged because of an exception Oct 2025, average area Band D 2026-27 £)
LPR=[('Barking and Dagenham','No',0,0,2198.51),('Barnet','Yes',940,0,2132.60),('Bexley','Yes',33,0,2366.36),('Brent','Yes',201,2,2235.27),
 ('Bromley','Yes',225,0,2140.04),('Camden','Yes',2286,0,2207.55),('City of London','Yes',1809,118,1329.56),('Croydon','Yes',129,101,2599.91),
 ('Ealing','Yes',616,218,2138.53),('Enfield','Yes',641,0,2267.67),('Greenwich','Yes',505,0,2107.86),('Hackney','Yes',387,634,2060.30),
 ('Hammersmith and Fulham','Yes',2160,0,1519.51),('Haringey','Yes',537,1080,2313.78),('Harrow','Yes',375,0,2511.07),('Havering','Yes',56,0,2424.66),
 ('Hillingdon','No',0,0,2045.46),('Hounslow','Yes',200,0,2185.56),('Islington','Yes',247,0,2108.15),('Kensington and Chelsea','No',0,0,1666.65),
 ('Kingston upon Thames','Yes',738,40,2609.20),('Lambeth','Yes',352,33,2047.11),('Lewisham','Yes',193,0,2237.33),('Merton','Yes',1131,0,2146.76),
 ('Newham','Yes',23,0,1944.23),('Redbridge','Yes',535,12,2294.58),('Richmond upon Thames','Yes',327,163,2486.10),('Southwark','Yes',700,42,1967.26),
 ('Sutton','Yes',151,11,2378.64),('Tower Hamlets','Yes',3231,4318,1837.78),('Waltham Forest','Yes',208,0,2386.96),('Wandsworth','Yes',1263,1180,1028.21),
 ('Westminster','Yes',10587,0,1049.55)]
LP_LATE={'Barking and Dagenham':LP_LBBD,'Kensington and Chelsea':LP_RBKC,'Hillingdon':LP_HILLM}
assert len(LPR)==33
LP_ENG=170299  # England total charged a second homes premium, Table 6.11 (Oct 2025)
LP_TOT=sum(r[2] for r in LPR);LP_EXC=sum(r[3] for r in LPR)
_lpm=lambda x:f'£{x:,.2f}'
_lpid=lambda n:'b-'+re.sub(r'[^a-z]+','-',n.lower()).strip('-')
_lptop=sorted(LPR,key=lambda r:-r[2])[:5];_lplo=min(LPR,key=lambda r:r[4]);_lphi=max(LPR,key=lambda r:r[4])
def _lprow(r):
    n,ap,ch,ex,bd=r
    since=('2025-26 (MHCLG)' if ap=='Yes' else f'1 Apr 2026 (<a href="{LP_LATE[n]}" rel="nofollow">council</a>)')
    return (f'<tr id="{_lpid(n)}"><td><b>{e(n)}</b></td><td>100%</td><td>{since}</td><td>{ch:,}</td><td>{ex:,}</td><td>{_lpm(bd)}</td><td><b>{_lpm(2*bd)}</b></td></tr>')
LPHD='<tr><th>Council</th><th>Premium 2026-27</th><th>Charged from</th><th>Second homes paying it (Oct 2025)</th><th>Not charged: exception (Oct 2025)</th><th>Band D 2026-27</th><th>Band D on a second home</th></tr>'
LPQ=[('Do all London boroughs charge the second homes premium?',f'Yes, all 33 London councils (the 32 boroughs and the City of London) have now decided to charge it, at 100%. In October 2025, 30 of them told MHCLG they were charging it in 2025-26. Barking and Dagenham, Hillingdon and Kensington and Chelsea started on 1 April 2026; each has said or decided its premium is 100%.'),
 ('How much is council tax on a second home in London?',f'A 100% premium doubles the bill. Using MHCLG\'s average Band D figures for 2026-27 (including the Greater London Authority precept), a Band D second home pays from {_lpm(2*_lplo[4])} a year in {_lplo[0]} to {_lpm(2*_lphi[4])} in {_lphi[0]}. Other bands are a fixed share of Band D, from 6/9 for Band A to 18/9 for Band H.'),
 ('Does my London short let pay the second homes premium?','It can. If the property is furnished and nobody\'s sole or main home, and it is on council tax, the council can charge the premium unless an exception applies. If you let your own home while you are away, it is still your main home, so the premium does not apply. A holiday let valued for business rates (available at least 140 nights and actually let at least 70 nights in the last 12 months) pays business rates instead of council tax, so no premium.'),
 ('Which exceptions could stop the premium?','The national exceptions (Classes E to L) include annexes treated as part of the main home, homes actively marketed for sale or let (up to 12 months), recent probate (up to 12 months), job-related homes, and seasonal homes where a planning condition limits use to holiday accommodation or stops year-round living. Apply to your borough with evidence.'),
 ('Which London council has the most second homes paying the premium?',f'Westminster, by a long way: {LPR[-1][2]:,} second homes were being charged the premium in October 2025, about {round(100*LPR[-1][2]/LP_TOT)}% of London\'s {LP_TOT:,}. Next were Tower Hamlets (3,231), Camden (2,286) and Hammersmith and Fulham (2,160).'),
 ('Where do the numbers come from?','Each council reports how many second homes it charges to MHCLG every October (Council Taxbase statistics). The 2025 release was published on 6 November 2025 and revised on 21 January 2026. Band D amounts come from MHCLG\'s Council Tax levels for 2026-27 (25 March 2026). We will update this page when the 2026 Council Taxbase release is out.'),
 ('Can I quote or reuse this table?',f'Yes. Please credit the UK Short-Let Rules Tracker and link to this page. The CSV download has the same rows. The figures are official statistics, summarised by us; check your bill and your council before relying on them.')]
def LPBUILD():
    fq='<div class="faq">'+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in LPQ)+'</div>'
    fld='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in LPQ]}).replace('</','<\\/')+'</script>'
    ld=json.dumps({'@context':'https://schema.org','@type':'Dataset','name':'London second homes council tax premium by borough','description':f'Second homes council tax premium for all 33 London councils: the rate in 2026-27, when each started, second homes paying it and homes excepted (Oct 2025, MHCLG Council Taxbase 2025), and the 2026-27 Band D bill with and without the premium (MHCLG Council Tax levels 2026-27).','url':SITE+LPF[:-5],'dateModified':C,'creator':{'@type':'Organization','name':'The UK Short-Let Rules team','url':SITE},'spatialCoverage':'Greater London, United Kingdom','temporalCoverage':'2025/2027','isAccessibleForFree':True,'isBasedOn':[LP_CTB,LP_CTL],'distribution':[{'@type':'DataDownload','encodingFormat':'text/csv','contentUrl':SITE+LPCSV}]}).replace('</','<\\/')
    bf=_io.StringIO();w=_csv.writer(bf)
    w.writerow(['council','premium_2026_27','charged_from','second_homes_charged_premium_oct_2025','not_charged_exception_oct_2025','band_d_2026_27_gbp','band_d_second_home_2026_27_gbp','source','checked'])
    for n,ap,ch,ex,bd in LPR:w.writerow([n,'100%','2025-26' if ap=='Yes' else '1 Apr 2026',ch,ex,f'{bd:.2f}',f'{2*bd:.2f}',(LP_CTBX if ap=='Yes' else LP_LATE[n])+' ; '+LP_CTL,C])
    open(LPCSV,'w',newline='').write(bf.getvalue())
    top=', '.join(f'{e(r[0])} ({r[2]:,})' for r in _lptop)
    b=(ANSWER('Do London boroughs charge the second homes premium?',f'Yes. All 33 London councils now charge a 100% second homes premium, so a furnished home that is nobody\'s main home pays double council tax. 30 were already charging it in 2025-26, according to their October 2025 returns to MHCLG, and Barking and Dagenham, Hillingdon and Kensington and Chelsea started on 1 April 2026. In October 2025, <b>{LP_TOT:,}</b> London second homes were paying it, {LPR[-1][2]:,} of them in Westminster. Holiday lets valued for business rates do not pay it.')
     +TOPICALERT('ldn-premium-alert','london-premium','Get an email when London second-home or short-let rules change',
       'We watch the London premium, the 90-night rule and the England-wide changes that apply in London (the national register, planning use classes, the visitor levy) against official sources. When MHCLG publishes new borough figures or a rule changes, we email you.',
       "Next dates for London hosts we're watching",_rowdates(lambda r:r[2] in ('All of England','England, Wales and Northern Ireland')),
       [('council:greater-london-all-boroughs','Greater London (all boroughs)',True),('nation:england','England',False)],'Your area',
       'Keep Greater London for London alerts, or pick All of England.',
       'We have no upcoming London dates logged right now. If the government or a borough announces a change, we\'ll email you.')
     +f'<h2 id="glance">At a glance</h2><ul><li><b>33 of 33</b> London councils have a 100% premium (the most an English council can charge): 30 charged it in 2025-26, the first year English councils could, and 3 started on 1 April 2026.</li>'
     +f'<li><b>{LP_TOT:,}</b> second homes in London were paying it in October 2025, {round(100*LP_TOT/LP_ENG)}% of the {LP_ENG:,} in England. Most: {top}.</li>'
     +f'<li><b>{LP_EXC:,}</b> more London second homes were not charged because an exception applied (October 2025), most in Tower Hamlets (4,318), Wandsworth (1,180) and Haringey (1,080).</li>'
     +f'<li>A Band D second home pays <b>{_lpm(2*_lplo[4])}</b> ({e(_lplo[0])}) to <b>{_lpm(2*_lphi[4])}</b> ({e(_lphi[0])}) a year in 2026-27.</li></ul>'
     +f'<h2 id="by-borough">London second homes premium by borough</h2><p>All 33 London billing authorities. "Band D on a second home" is the 2026-27 average Band D bill doubled by the 100% premium. Counts are what each council reported to MHCLG in October 2025, before the three newest premiums started.</p>'
     +f'<div class="tw"><table class="stk">{LPHD}{"".join(_lprow(r) for r in LPR)}</table></div>'
     +f'<p class="small">Sources: second homes counts and premium status, <a href="{LP_CTB}" rel="nofollow">MHCLG Council Taxbase 2025</a> (local authority data, Tables 6.06, 6.11 and 6.12, revised 21 Jan 2026). Band D, <a href="{LP_CTL}" rel="nofollow">MHCLG Council Tax levels 2026-27</a> (Table 9: average area Band D for two adults, including the GLA, adult social care and parish precepts). 1 April 2026 starts: <a href="{LP_LBBD}" rel="nofollow">Barking and Dagenham</a> (100% extra charge), <a href="{LP_RBKC}" rel="nofollow">Kensington and Chelsea</a> (premium of 100%), Hillingdon (Full Council approved an additional 100% on 22 Jan 2026, <a href="{LP_HILLM}" rel="nofollow">minutes</a>; <a href="{LP_HILL}" rel="nofollow">council page</a>). Still 100% in 2026-27, spot-checked 5 Nov 2026: <a href="{LP_WCAB}" rel="nofollow">Westminster</a> (Cabinet report to Full Council, 4 Mar 2026), <a href="{LP_CAM}" rel="nofollow">Camden</a> (2026/27 council tax guide) and <a href="{LP_TH}" rel="nofollow">Tower Hamlets</a> (council page). A premium decision stays in place until the council changes it before a new financial year, but we have not re-checked every other borough\'s own page for 2026-27.</p>'
     +'<h2 id="short-lets">What it means for London short lets</h2><ul>'
     +'<li><b>Your own home, let while you are away:</b> still your main home, so no second homes premium. The <a href="london-90-night-counter.html">90-night rule</a> still limits whole-home short letting without planning permission.</li>'
     +'<li><b>A furnished flat that is nobody\'s main home, on council tax:</b> the borough charges 200% council tax unless an exception fits.</li>'
     +f'<li><b>Valued for business rates:</b> a let available at least 140 nights and actually let at least 70 nights in the last 12 months is valued for business rates, so it pays no council tax premium (<a href="{EN_BR}" rel="nofollow">GOV.UK</a>).</li>'
     +f'<li><b>Exceptions:</b> Classes E to L, including annexes, homes marketed for sale or let (12 months), probate and planning-restricted holiday homes (<a href="{PG}" rel="nofollow">MHCLG guidance</a>). See the <a href="england-second-homes-council-tax-premium.html">England second homes premium guide</a>.</li></ul>'
     +f'<h2 id="cite">Use this table</h2><div class="box"><p>Journalists, agents and researchers are welcome to quote or link to this table. Please credit: <i>UK Short-Let Rules Tracker, "London second homes council tax premium by borough", {SITE}{LPF[:-5]}, checked {_fdate(C)}</i>.</p><p><a class="btn" href="{LPCSV}" download>Download the table (CSV)</a> <span class="small">All 33 rows, with the official source for each.</span></p></div>'
     +'<h2 id="ldn-faq">Common questions</h2>'+fq
     +'<p class="small">More: <a href="councils/greater-london-all-boroughs.html">Greater London council page</a> · <a href="london-90-night-counter.html">London 90-night counter</a> · <a href="second-homes-council-tax-premium-by-council.html">Second homes premium by council (UK table)</a> · <a href="england-second-homes-council-tax-premium.html">England second homes premium guide</a> · <a href="buyer-due-diligence-checker?council=greater-london-all-boroughs">Buying in London? Due-diligence checker</a>.</p>'
     +'<p class="small"><b>Not tax advice.</b> Compiled by the UK Short-Let Rules team from official statistics and council sources. Your council decides whether a home is a second home and whether an exception applies, so check with them before acting.</p>')
    page(LPF,'London second homes council tax premium by borough',b,desc=f'All 33 London councils charge a 100% second homes premium in 2026-27. Borough table: homes paying, exceptions and the Band D bill on a second home, with a CSV.',full_title='London Second Homes Council Tax Premium: All 33 Boroughs',head='<script type="application/ld+json">'+ld+'</script>'+fld)
LPBUILD()
