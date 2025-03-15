Netflix Example - https://todayssolutionsinc.com/

Required tools: subfinder, assetfinder, httpx-toolkit, subzy, katana

1) prepare targets folder
   (mkdir ...)

2) sudo subfinder -d netflix.com -all > subdomain.txt
   (in first cmd)

3) sudo assetfinder -subs-only netflix.com > subdomain1.txt
   (in second cmd)

4) sort -u subdomain.txt subdomain1.txt > mainsubdomain.txt
   (in first cmd)

5) cat subdomain.txt | wc -l
   ---> watch all the subdomains
   (in first cmd)

6) cat mainsubdomain.txt | sudo httpx-toolkit > alive_subdomain.txt
   (in first cmd)

7) sudo subzy run --targets mainsubdomain.txt
   ---> go to number (15) for subdomain take over
   (in second cmd)

8) cat alive_subdomain.txt | sudo httpx-toolkit -sc > alive_domain_code.txt
   (in first cmd)

9) cat alive_domain_code.txt
   ---> try all 200, 301, 302
   (in first cmd)

10) sudo katana -u https://brand.netflix.com -jc -o allurls.txt
    ---> instead of this link try one from the alive_domain_code.txt
    ---> so you can find all javascript files
    (in first cmd)

11) sudo katana -u https://brand.netflix.com -o allurls.txt
    (in first cmd)

12) sudo katana -u alive_domain_code.txt -d 5 -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -o allurls.txt
    (in first cmd)

13) sudo katana -u https://sec-oc.netflix.com -d 5 -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -o allurls.txt
    ---> link from alive_domain_code.txt
    ---> open .png links and try /etc/passwd or path traversel (example: https://roomeo.netflix.com/img/../../../../../etc/passwd
    (in first cmd)

14) cat allurls.txt | grep "=*"
    ---> if you find this parameter "=" try xss and sql injection
    (in first cmd)

15) DOMAIN TAKE OVER
