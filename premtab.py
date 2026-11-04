# ---- Citable table: second homes council tax premium by council (4 Nov 2026) ----
# Pulls together the second homes premium already on each council page (in its Fees card, or its Visitor levy card where noted), sourced there.
# One row per council page that covers the premium; level, bill and summary set by hand below from that page's text. Directory-only councils (PICK_EXCL) are left out.
# exec'd from build.py BEFORE the council pages (PRMCMP adds the card foot link) and PRMBUILD() is called after planmap.py. Also writes a CSV copy.
import csv as _csv,io as _io,html as _H0
PRF='second-homes-council-tax-premium-by-council.html';PRCSV='second-homes-council-tax-premium-by-council.csv'
PRST={'hi':('Above 100%','p-in'),'max':('100% (double)','p-coming'),'low':('Below 100%','p-proposed'),'none':('No premium','p-announced'),'plan':('Agreed, not yet charged','p-proposed'),'unv':('Unclear (check with council)','p-announced')}
# slug: (level key, premium text, total bill text, since text, summary html, card holding the premium on the council page, index of its official source)
PRM={
# England (council pages: Fees card unless noted)
 'cornwall':('max','100%','200%','1 Apr 2025','Exceptions include homes with holiday-only planning conditions.','levy',0),
 'north-yorkshire':('max','100%','200%','1 Apr 2025','Decided 21 Feb 2024 and kept unchanged in the 2026-27 council tax resolution. Homes with a planning restriction of at least 28 days (Class A) get no discount and no premium.','fees',0),
 'northumberland':('max','100%','200%','1 Apr 2025','Approved by Full Council on 21 Feb 2024. The 12-month marketing exceptions run from the date the home was first marketed.','fees',0),
 'westmorland-and-furness':('max','100%','200%','1 Apr 2025','Decided 22 Feb 2024; also applies to homes owned by businesses. Discretionary local exceptions in its 2025 to 2026 policy.','fees',0),
 'cumberland':('max','100%','200%','1 Apr 2025','Adopted 6 Mar 2024. You must apply for an exception, in the area where the second home is.','fees',0),
 'north-norfolk':('max','100%','200%','1 Apr 2025','Decided 22 Nov 2023. Holiday lets not on the business rates list pay council tax as a second home and may pay the premium.','fees',0),
 'dorset':('max','100%','200%','1 Apr 2025','Agreed at the Feb 2024 budget meeting. Applies from day one, with no minimum period as a second home.','fees',0),
 'south-hams':('max','100%','200%','1 Apr 2025','Added to bills automatically (public notice 2 Mar 2024). Local discretionary exceptions set for 2025-26, e.g. agricultural occupancy conditions.','fees',0),
 'north-devon':('max','100%','200%','1 Apr 2025','Decided 17 Jan 2024; includes furnished homes with a planning restriction on occupation unless an exception applies.','fees',0),
 'isle-of-wight':('max','100%','200%','1 Apr 2025','Power adopted Feb 2024. Claim exceptions on the council\'s Empty and Second Home Review Form.','fees',0),
 'east-suffolk':('max','100%','200%','1 Apr 2025','Approved Feb 2024. A home marketed for sale is excepted for up to 24 months (the national rule is 12).','fees',0),
 'somerset':('max','100%','200%','1 Apr 2025','Full Council reaffirmed it on 20 Dec 2023; includes furnished homes with a planning restriction on occupation.','fees',0),
 'liverpool':('max','100%','200%','Not stated','The council page confirms second homes pay twice the normal charge, but not when this was decided (the national power allows it from 1 Apr 2025).','fees',0),
 'sefton':('max','100%','200%','1 Apr 2025','Approved by Full Council on 18 Jan 2024.','fees',0),
 'torridge':('max','100%','200%','1 Apr 2025','Voted in on 22 Jan 2024; no premium was charged before.','fees',0),
 'east-lindsey':('max','100%','200%','1 Apr 2025','Approved 28 Feb 2024; added to your bill automatically.','fees',0),
 'cotswold':('max','100%','200%','1 Apr 2025','Voted unanimously on 20 Mar 2024. A second home usable all year with no planning restriction pays it.','fees',0),
 'east-devon':('max','100%','200%','1 Apr 2025','Approved 21 Feb 2024; the council ringfences its share for housing and will review it in 2029.','fees',0),
 'torbay':('max','100%','200%','1 Apr 2025','Adopted 5 Dec 2024, national exceptions only. A June 2026 review said 16 homes that would have paid it moved to business rates in a year.','fees',0),
 'brighton-and-hove':('max','100%','200%','1 Apr 2025','Approved 1 Feb 2024. Since 1 Apr 2026, serviced accommodation (short to medium stays with hotel-like services) is an exception.','fees',0),
 'bath-and-north-east-somerset':('max','100%','200%','1 Apr 2025','Resolved unanimously on 30 Nov 2023. The sale or letting exception runs from the date first advertised and can be used only once.','fees',0),
 'new-forest':('max','100%','200%','1 Apr 2025','Determined 26 Feb 2024; about 1,210 homes in the 2026/27 tax base. No discretion beyond the listed exceptions.','fees',0),
 'west-devon':('max','100%','200%','1 Apr 2025','Resolved 20 Feb 2024. Local discretionary exceptions, e.g. agricultural occupancy conditions and some staff accommodation.','fees',0),
 'teignbridge':('max','100%','200%','1 Apr 2025','Resolved 27 Feb 2024. A Sep 2026 review found premiums charged on about 81.7% of 891 furnished empty homes; a report to Full Council to review and reaffirm it is due.','fees',0),
 'city-of-york':('max','100%','200%','1 Apr 2025','Approved 22 Feb 2024. Not charged on homes with an occupancy restriction for part of the year.','fees',0),
 'derbyshire-dales':('max','100%','200%','1 Apr 2025','Approved (announced 4 Mar 2024) and confirmed 3 Mar 2025. Local exceptions include age-restricted homes being marketed for sale or rent.','fees',0),
 'bournemouth-christchurch-and-poole':('max','100%','200%','1 Apr 2025','Determination approved 9 Jan 2024; national exceptions only.','fees',0),
 'isles-of-scilly':('max','100%','200%','1 Apr 2025','In the budget approved 22 Feb 2024. Local exception for staff accommodation for island employers.','fees',0),
 'canterbury':('max','100%','200%','1 Apr 2025','First approved 4 Jan 2024; national exceptions only.','fees',0),
 'thanet':('max','100%','200%','1 Apr 2025','Decided 11 Jan 2024 and continued for 2026/27. Its guidance says the marketed-to-let exception excludes holiday lets.','fees',0),
 'folkestone-and-hythe':('max','100%','200%','1 Apr 2025','National exceptions; send evidence to the council, which may visit to check.','fees',0),
 'rother':('max','100%','200%','1 Apr 2025','Approved 26 Feb 2024.','fees',0),
 'chichester':('max','100%','200%','1 Apr 2025','Decided Mar 2024; the 2026/27 bill guidance confirms 100%. National exceptions only.','fees',0),
 'kings-lynn-and-west-norfolk':('max','100%','200%','1 Apr 2025','Agreed Jan 2024, re-approved for 2026/27. More than 3,000 second homes. A planning condition stopping main-residence use also counts as an exception.','fees',0),
 'great-yarmouth':('max','100%','200%','1 Apr 2025','Resolved 14 Dec 2023. More than 1,000 second homes; 25% of the money raised goes back to the districts most affected.','fees',0),
 'wealden':('max','100%','200%','1 Apr 2025','Agreed 21 Feb 2024 (Cabinet 7 Feb 2024).','fees',0),
 'stratford-on-avon':('plan','100% from 1 Apr 2027','100% now, 200% from 1 Apr 2027','1 Apr 2027','Agreed by Cabinet and Council on 23 Feb 2026 (859 second homes). No second homes discount since 2013. Scrutiny was told the council could still decide not to go ahead before 2027/28.','fees',0),
 'oxford':('max','100%','200%','1 Apr 2025','Applies to most second homes; apply for an exception online.','fees',0),
 'cambridge':('max','100%','200%','1 Apr 2025','Agreed 25 Mar 2024. The council says it includes homes used for short-term holiday rental.','fees',0),
 'bristol':('max','100%','200%','1 Apr 2025','Decided by Cabinet (23 Jan 2024) and Council (28 Feb 2024). If an exception is granted, the standard charge is still payable.','fees',0),
 'manchester':('max','100%','200%','1 Apr 2025','Agreed 17 Jan 2024. Charged from day one on a home used as a second home, or after 12 months on a furnished home nobody lives in.','fees',0),
 'blackpool':('max','100%','200%','1 Apr 2025','Agreed 21 Feb 2024. The council says it can include short-term holiday lets and furnished rentals empty between lets.','fees',0),
# Wales
 'pembrokeshire':('hi','125%','225%','1 Apr 2026','Down from 200% (2024-25) and 150% (2025-26). The council has confirmed 125% for 2027-28.','fees',0),
 'isle-of-anglesey':('max','100%','200%','In force 2026/27','Set by Full Council on 5 Mar 2026 with the 2026/27 council tax. The council\'s second homes page still shows older wording.','fees',2),
 'conwy':('hi','150%','250%','2026-27 and 2027-28','Retained for 2026-27 and 2027-28 (decided 23 Oct 2025). No discount for second homes or holiday homes.','fees',0),
 'ceredigion':('hi','150%','250%','1 Apr 2025','100% from 1 Apr 2024, then 150%. Covers self-catering units that fail the business rates criteria.','fees',0),
 'powys':('low','75%','175%','1 Apr 2023','Unchanged for 2026-27. 235 more self-catering units moved into council tax after failing the 252/182-day letting test.','fees',0),
 'denbighshire':('hi','150%','250%','1 Apr 2025','100% from 1 Apr 2024. Full Council on 8 Jul 2025 kept 150% from 1 Apr 2026.','fees',0),
 'carmarthenshire':('max','100%','200%','1 Apr 2025','50% from 1 Apr 2024, then 100% for all second homes.','fees',0),
 'swansea':('max','100%','200%','1 Apr 2021','The marketed-for-let exception (Class 2) covers tenancies of at least 6 months, not holiday or Airbnb lets.','fees',0),
 'monmouthshire':('max','100%','200%','1 Apr 2024','Unchanged for 2026/27. Local exception: a property moving from business rates to council tax is free of the premium for 12 months.','fees',0),
 'vale-of-glamorgan':('max','100%','200%','1 Apr 2024','Reaffirmed by Cabinet on 18 Dec 2025 and set by Council for 2026/27.','fees',0),
 'wrexham':('low','50%','150%','1 Apr 2017','Lower than most Welsh councils that charge one; 71 homes paying in the 2026/27 tax base.','fees',0),
 'flintshire':('max','100%','200%','1 Apr 2023','Decided 13 Dec 2022, kept for 2026/27. No discount on second homes.','fees',0),
 'bridgend':('hi','200%','300%','1 Apr 2026','100% from 1 Apr 2024, rising to 200% after two years (decided 20 Sep 2023). One of the highest-charging councils in Wales.','fees',0),
 'newport':('max','100%','200%','1 Apr 2025','Still charged in 2026/27. The council says it can include short-term holiday lets that pay council tax rather than business rates.','fees',0),
 'neath-port-talbot':('max','100%','200%','1 Apr 2025','Local exception D (from 1 Apr 2026): the premium can be waived for 6 months when a self-catering let moves from business rates to council tax.','fees',0),
 'rhondda-cynon-taf':('max','100%','200%','1 Apr 2024','Agreed Jan 2023. Second homes paying it rose from 491 (Apr 2023) to 647 (Mar 2024).','fees',0),
 'caerphilly':('max','100%','200%','1 Apr 2025','Agreed Mar 2024; 175 second homes paying in 2026/27. No local exception for lets moving from business rates.','fees',0),
 'torfaen':('none','None','100%','','One of two Welsh councils not charging a second homes premium in 2026/27. It says it is considering one; a first decision must be made at least a year before it starts.','fees',0),
 'blaenau-gwent':('unv','100% or none','200% or 100%','1 Apr 2026 (council page)','Sources disagree: the council page says 100% from 1 Apr 2026, but its 2026/27 return to the Welsh Government shows no second homes paying it. '+U+' Ask the council before you budget.','fees',0),
 'merthyr-tydfil':('max','100%','200%','1 Apr 2024','Kept for 2025/26 and 2026/27; 171 second homes paying in 2026/27.','fees',0),
# Scotland (council pages: Visitor levy card)
 'north-ayrshire':('max','100%','200%','1 Apr 2025','Includes Arran and Cumbrae. A let that qualifies for business rates is not charged council tax.','levy',2),
 'south-lanarkshire':('max','100%','200%','1 Apr 2024','From the council\'s council tax page.','levy',3),
 'east-renfrewshire':('unv','Up to 100% (proposed)','Up to 200%','1 Apr 2024 (proposed)','A Dec 2023 Cabinet report proposed removing the 10% discount and charging up to 100% from 1 Apr 2024; we could not confirm the final rate on the council\'s website. '+U,'levy',2),
}
def PRMCMP(h,c,s,k):
    """Council pages in the premium table: foot link in the card that holds the premium (Fees, or Visitor levy). Never on PICK_EXCL."""
    if s in PICK_EXCL or s not in PRM or PRM[s][5]!=k: return h
    return h[:-len('</section>')]+'<p class="small"><a href="../second-homes-council-tax-premium-by-council.html" data-cta="council-premium">Compare second homes council tax premiums across UK councils</a></p></section>'
def PRMBUILD():
    global PRR,_prn
    _cs={_sl(c):c for c in d['councils'] if c['verified'] and _sl(c) not in PICK_EXCL and _sl(c) in CX}
    assert all(k in _cs for k in PRM),'PRM slug not a listed council'
    for k,v in PRM.items():
        assert re.search(r'premium|surcharge',CX[k][v[5]][0],re.I),k  # the card really carries the premium
    PRR=[]
    for k,(lv,pm,bill,since,tx,card,si) in PRM.items():
        c=_cs[k];PRR.append(dict(slug=k,name=c['name'],nation=c['nation'],lv=lv,pm=pm,bill=bill,since=since,tx=tx,src=CX[k][card][1][si]))
    PRR.sort(key=lambda r:({'England':0,'Wales':1,'Scotland':2}[r['nation']],r['name'].replace('City of ','')))
    _prn={k:sum(1 for r in PRR if r['lv']==k) for k in PRST}
    _nn=lambda n,k=None:sum(1 for r in PRR if r['nation']==n and (k is None or r['lv']==k))
    tot=len(PRR);en,wa,sc=_nn('England'),_nn('Wales'),_nn('Scotland')
    _miss=sorted([c['name'] for s,c in _cs.items() if s not in PRM and c['nation'] in ('England','Wales')])
    sp=lambda k:f'<span class="pill {PRST[k][1]}">{PRST[k][0]}</span>'
    tr=lambda r:f'<tr><td><a href="councils/{r["slug"]}.html">{e(r["name"])}</a></td><td data-label="Nation">{r["nation"]}</td><td data-label="Second homes premium">{sp(r["lv"])} {e(r["pm"])}</td><td data-label="Bill on a second home">{e(r["bill"])}</td><td data-label="Since">{e(r["since"]) or "–"}</td><td data-label="Notes">{r["tx"]} <a href="{e(r["src"])}" rel="nofollow">Source</a></td></tr>'
    hd='<tr><th>Council</th><th>Nation</th><th>Second homes premium</th><th>Bill on a second home</th><th>Since</th><th>Notes</th></tr>'
    wal=[r for r in PRR if r['nation']=='Wales']
    key=[r for r in PRR if r['lv']!='max']
    key.sort(key=lambda r:(['hi','low','none','plan','unv'].index(r['lv']),r['nation'],r['name']))
    Q=[('What is the second homes council tax premium?','It is extra council tax a council can charge on a second home: a home that is substantially furnished but is nobody\'s sole or main residence. Each council decides whether to charge it and at what rate. In England the maximum is 100% (double council tax) from 1 April 2025, in Wales it is up to 300% (four times) since 1 April 2023, and in Scotland councils can charge up to 100% since 1 April 2024.'),
       ('Do holiday lets pay the second homes premium?','Only if the let is on council tax. A holiday let valued for business rates does not pay council tax, so the premium does not apply. In England that means available for at least 140 nights and actually let for at least 70 nights in the last 12 months; in Wales, at least 252 nights available and 182 let. Lets that miss the test move to council tax, where the premium can apply unless an exception fits.'),
       ('Which councils charge the highest second homes premium?',f'Among the {tot} councils in this table, the highest is Bridgend at 200% (a bill of 300%) from 1 April 2026, followed by Conwy, Ceredigion and Denbighshire at 150% and Pembrokeshire at 125%. Every English council in the table that charges the premium charges the 100% maximum.'),
       ('Which councils do not charge a second homes premium?','In this table, Torfaen charges no second homes premium in 2026/27, and Stratford-on-Avon has agreed a 100% premium that starts on 1 April 2027. Blaenau Gwent is unclear because its own sources disagree, so ask the council.'),
       ('Can I use or quote this table?','Yes. Please credit the UK Short-Let Rules Tracker and link to this page. Each row links to the official source and to the council page with the full wording, exceptions and contacts. It is a summary of general information, not tax advice, so check your bill and your council before relying on it.')]
    fq='<div class="faq">'+''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in Q)+'</div>'
    fld='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in Q]}).replace('</','<\\/')+'</script>'
    ld=json.dumps({'@context':'https://schema.org','@type':'Dataset','name':'Second homes council tax premium by council (UK)','description':f'Second homes council tax premium for {tot} UK council areas ({en} in England, {wa} in Wales, {sc} in Scotland): the premium rate, the total bill on a second home, the start date and notes for holiday lets, each with an official source.','url':SITE+PRF[:-5],'dateModified':C,'creator':{'@type':'Organization','name':'The UK Short-Let Rules team','url':SITE},'spatialCoverage':'United Kingdom','isAccessibleForFree':True,'distribution':[{'@type':'DataDownload','encodingFormat':'text/csv','contentUrl':SITE+PRCSV}]}).replace('</','<\\/')
    bf=_io.StringIO();w=_csv.writer(bf)
    w.writerow(['council','nation','status','second_home_premium','bill_on_second_home','since','notes','council_page','official_source','checked'])
    for r in PRR:w.writerow([r['name'],r['nation'],PRST[r['lv']][0],r['pm'],r['bill'],r['since'],_H0.unescape(re.sub(r'<[^>]+>','',r['tx'])),SITE+'councils/'+r['slug'],r['src'],C])
    open(PRCSV,'w',newline='').write(bf.getvalue())
    hi=_prn['hi'];mx=_prn['max']
    b=(ANSWER('How much council tax do second homes pay in each council?',f'Most councils now charge a second homes premium. In England councils can add up to 100% (double council tax) from 1 April 2025, and {_nn("England","max")} of the {en} English councils below do, with one more starting in April 2027. Welsh councils can add up to 300%: of the {wa} Welsh councils below, {_nn("Wales","hi")} charge more than 100%, {_nn("Wales","max")} charge 100%, {_nn("Wales","low")} charge less, {_nn("Wales","none")} charges none and {_nn("Wales","unv")} is unclear. Holiday lets that pay business rates instead of council tax do not pay it.')
     +PICK('premium-table',aid='top-alerts',tag='div')
     +'<h2 id="not-100">Councils that charge more, less or not yet</h2><p>Every council below charges something other than the standard 100% premium, or its rate is unclear. Statuses: '+' '.join(sp(k) for k in ('hi','max','low','none','plan','unv'))+'.</p>'
     +f'<div class="tw"><table class="stk prt">{hd}{"".join(tr(r) for r in key)}</table></div>'
     +f'<h2 id="counts">At a glance</h2><ul><li><b>{tot}</b> council areas in this table: {en} in England, {wa} in Wales and {sc} in Scotland.</li><li><b>{mx}</b> charge a 100% premium (double council tax).</li><li><b>{hi}</b> charge more than 100%, all in Wales (125% to 200%).</li><li><b>{_prn["low"]}</b> charge less than 100% (Powys 75%, Wrexham 50%).</li><li><b>{_prn["none"]}</b> charges none, <b>{_prn["plan"]}</b> has agreed one that starts on 1 Apr 2027 and <b>{_prn["unv"]}</b> are unclear.</li></ul>'
     +'<h2 id="national-rules">The national rules behind the table</h2><ul>'
     +f'<li><b>England:</b> from 1 April 2025 councils can charge up to 100% extra on second homes (furnished, nobody\'s sole or main residence), and must decide at least a year before it starts. Exceptions Classes E to L include annexes, homes marketed for sale or let (12 months) and holiday-only or seasonal homes restricted by planning (<a href="{PG}" rel="nofollow">MHCLG guidance</a>). A let valued for business rates (140 nights available, 70 let) does not pay it. <a href="england-second-homes-council-tax-premium.html">England premium guide</a>.</li>'
     +f'<li><b>Wales:</b> since 1 April 2023 councils can charge up to 300% (<a href="{WG}" rel="nofollow">Welsh Government guidance</a>). A self-catering let stays on business rates only if it is available for 252 nights and let for 182. Class 6 excepts homes a planning condition limits to holiday use. <a href="wales-second-homes-council-tax-premium.html">Wales premium guide</a>.</li>'
     +'<li><b>Scotland:</b> since 1 April 2024 councils can charge up to 100% (double) on second homes; the Scottish Government said 29 of 32 councils confirmed they would, with Falkirk, Glasgow City and North Ayrshire not doubling it in 2024-25 (<a href="https://www.gov.scot/news/council-tax-on-second-homes/" rel="nofollow">gov.scot, 31 Mar 2024</a>). Our Scottish council pages track the premium for only 3 councils so far, so the others are not in the table. <a href="scotland-business-rates-checker.html">Scotland business rates or council tax checker</a>.</li>'
     +'<li><b>Northern Ireland:</b> no second homes premium is listed on this site; we have no council pages there yet. <a href="northern-ireland.html">Northern Ireland rules</a>.</li></ul>'
     +(f'<p class="small">Not in the table because their council page does not cover the premium yet: {", ".join(e(x) for x in _miss)}.</p>' if _miss else '')
     +f'<h2 id="all-councils">All {tot} council areas</h2><p>Every council page that covers the premium, with its rate and official source. Open a council page for the exceptions, how to claim one and a free alert when the rules change.</p>'
     +COLLAPSE(f'Show all {tot} council areas',f'<div class="tw"><table class="stk prt">{hd}{"".join(tr(r) for r in PRR)}</table></div>',filt='Filter by council, nation or rate')
     +f'<h2 id="cite">Use this table</h2><div class="box"><p>Journalists, agents and researchers are welcome to quote or link to this table. Please credit: <i>UK Short-Let Rules Tracker, "Second homes council tax premium by council", {SITE}{PRF[:-5]}, checked {_fdate(C)}</i>.</p><p><a class="btn" href="{PRCSV}" download>Download the table (CSV)</a> <span class="small">Same rows as above, with the council page and official source for each.</span></p></div>'
     +'<h2 id="pr-faq">Common questions</h2>'+fq
     +'<p class="small">More: <a href="england-second-homes-council-tax-premium.html">England second homes premium guide</a> · <a href="wales-second-homes-council-tax-premium.html">Wales second homes premium guide</a> · <a href="occupancy-threshold-tracker.html">Business rates or council tax? Occupancy threshold tracker</a> · <a href="short-let-planning-permission-by-council.html">Planning permission by council</a> · <a href="buyer-due-diligence-checker.html">Buying a holiday let? Due-diligence checker</a> · <a href="councils.html">All councils</a>.</p>'
     +'<p class="small"><b>Not tax advice.</b> Compiled by the UK Short-Let Rules team from each council page\'s official sources; summaries are shortened, so read the council page and check with the council before acting. Items marked UNVERIFIED have not been confirmed against an official source.</p>'+FILTJS)
    page(PRF,'Second homes council tax premium by council (UK)',b,desc=f'Second homes council tax premium in {tot} UK councils: rates from 0% to 200%, the bill, start dates and holiday-let notes, with official sources and a CSV.',full_title='Second homes council tax premium by council: UK table',head='<script type="application/ld+json">'+ld+'</script>'+fld)
