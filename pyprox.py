import requests
import bs4
import splinter
import json

# Navigate to US proxy
us_proxy = 'https://www.us-proxy.org/'
browser = splinter.Browser('chrome', headless=True)
browser.visit(us_proxy)

def scrape_page(browser):

	# Identify the table, header and rows
	tab = browser.find_by_css('div[id="proxylisttable_wrapper"]')[0]
	header = tab.find_by_tag('thead')
	rows = list(tab.find_by_tag('tr'))[1:]

	# Collect the column names
	columns=[]
	for cell in header.find_by_tag('th'):
	    columns.append(cell.html)

	# Collect the proxy information
	proxy_list = []
	for row in rows:
	    proxy = {}
	    for i,cell in enumerate(row.find_by_tag('td')):
	        proxy[columns[i]] = cell.html
	    proxy_list.append(proxy)

	return proxy_list


def pull_proxies(pages=1):
	us_proxy = 'https://www.us-proxy.org/'
	browser = splinter.Browser('chrome', headless=True)
	browser.visit(us_proxy)


	count = 0
	master_list=[]
	while count < pages:
		master_list.append(scrape_page(browser))
		count += 1

	with open('proxies.json', 'w') as wfile:
		json.dump(master_list, wfile)

	print("Done!")


pull_proxies()