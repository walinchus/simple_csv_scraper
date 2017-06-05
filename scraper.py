import scraperwiki
import csv
data = scraperwiki.scrape('https://www.sos.state.co.us/pubs/charities/reports/2016/tables/Table2-PaidSolicitorSummary2016.csv')

reader = csv.DictReader(data.splitlines())

for row in reader:
    for key, value in row.iteritems():
        print key
    #row['Actual Funding Award'] = row['Actual Funding Award'].decode("latin-1")
   #row['Annual Total 2012/2013'] = row['Annual Total 2012/2013'].decode("latin-1")
    #row['Annual Total 2013/2014'] = row['Annual Total 2013/2014'].decode("latin-1")
    #row['Annual Total2014/2015'] = row['Annual Total2014/2015'].decode("latin-1")
    #row['Overall Total Paid'] = row['Overall Total Paid'].decode("latin-1")
    print row['Ref. No.']
    scraperwiki.sqlite.save(['Ref. No.'], row)
