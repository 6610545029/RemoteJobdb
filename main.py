import sqlite3
import pandas as pd
con = sqlite3.connect("RemoteJob.db")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS JobAppli")
cur.execute("CREATE TABLE JobAppli(id, jobSlug, jobTitle, companyName, jobIndustry, jobType, jobGeo, jobLevel, jobExcerpt, pubDate, annualSalaryMin, annualSalaryMax)")
cur.execute("""
    INSERT INTO JobAppli VALUES
    (
      107177,
      "107177-site-reliability-engineer-emea",
      "Senior Software Engineer, Privacy",
      "Chainlink Labs",
      "Software Engineering",
      "full-time",
      "Anywhere",
      "Senior",
      "Join a brand new team as the first engineer focused on embedding privacy-enhancing technologies into the Chainlink product stack. This role spans the development of both off-chain and on-chain privacy solutions to enhance the Chainlink runtime Environment. The mission is to introduce privacy solutions at every layer of Chainlink&amp;#8217;s operations, ensuring robust, customer-centric implementations to&amp;#8230;",
      "2025-05-07 06:25:24",
      0,
      100000
    ), 
    (
      112046,
      "112046-senior-java-developer-2",
      "Senior Java Developer (Tiger Team)",
      "Semrush",
      "Programming",
      "full-time",
      "Cyprus,  Czechia,  Poland,  Spain",
      "Senior",
      "We are Semrush, a global Tech company developing our own product – a platform for digital marketers. Are you ready to be a part of it? This is your chance! We’re hiring for Senior Java Developer (Tiger Team). Tasks in the role Manage the full feature development lifecycle: gather requirements, design architecture, coordinate contracts/interfaces with&amp;#8230;",
      "2025-05-07 06:22:14",
      "None",
      "None"
    ),
    (
      115350,
      "115350-sales-associate",
      "Strategic Sales Manager - DACH",
      "Adaptavist",
      "Sales",
      "full-time",
      "Germany",
      "Any",
      "The Strategic Sales Manager will play a key role in the Adaptavist Sales Process, and managing this end-to-end. This role will work with various teams across the business to define solutions for our clients, guide the production of proposals which oversee our commercial approach and solution offering, as well as manage the client through the&amp;#8230;",
      "2025-05-07 06:20:45",
      121000,
      154000
    ),
    (
      116064,
      "116064-hr-business-partner-2",
      "HR Business Partner",
      "WorkWave",
      "HR &amp; Recruiting",
      "full-time",
      "USA",
      "Any",
      "WorkWave is seeking an HR Business Partner (HRBP) to play a strategic role in aligning business objectives with employees and management within designated business units. This position partners across HR functions to provide value-added services that support business goals. The HRBP is expected to have a deep understanding of the business unit&amp;#8217;s financial status, culture,&amp;#8230;",
      "2025-05-07 06:19:33",
      150000,
      240000
    ),
    (
      117360,
      "117360-customer-success-consultant-4",
      "Customer Success Consultant",
      "Granicus",
      "Customer Success",
      "full-time",
      "USA",
      "Any",
      "The Customer Success Consultant is accountable for our clients&amp;#8217; adoption of our growing suite of SaaS solutions and services across client segment tiers, driving visible value aligned with our clients&amp;#8217; business outcomes. As a consultant, you will act as a powerful client advocate, providing exceptional customer service so that our clients can deliver high-quality civic&amp;#8230;",
      "2025-05-07 06:18:40",
      245000,
      265000
    ),
    (
      117358,
      "117358-senior-software-engineer-13",
      "Senior Software Engineer",
      "NationBuilder",
      "Software Engineering",
      "full-time",
      "USA",
      "Senior",
      "Our engineering team dedicates itself to continuous learning and improvement. We optimize for rapid, agile development with engineers deploying to production many times a day. To find and build the best solutions, we expect our teams to iterate. From the introduction of minimum viable products to the release of more mature features, Engineers must actively&amp;#8230;",
      "2025-05-07 05:28:49",
      "None",
      "None"
    ),
    (
      117356,
      "117356-senior-content-designer-3",
      "Senior Content Designer",
      "Paylocity",
      "Content &amp; Editorial",
      "full-time",
      "USA",
      "Senior",
      "This is a fully remote position, allowing you to work from home or location of record within the U.S. with no in-office requirements.  You must be available five days per week during designated work hours.  The work arrangement for this role is subject to change based on business needs and individual performance. This may include&amp;#8230;",
      "2025-05-07 05:26:49",
      "None",
      "None"
    ),
    (
      116065,
      "116065-recruiter-business",
      "Recruiter (Business)",
      "Revolut",
      "HR &amp; Recruiting",
      "full-time",
      "Brazil,  Mexico,  Poland,  Portugal,  Romania,  Spain",
      "Any",
      "People deserve more from their money. More visibility, more control, and more freedom. Since 2015, Revolut has been on a mission to deliver just that. Our powerhouse of products — including spending, saving, investing, exchanging, travelling, and more — help our 50+ million customers get more from their money every day. As we continue our&amp;#8230;",
      "2025-05-07 05:20:54",
      105000,
      120000
    ),
    (
      117343,
      "117343-onboarding-specialist-9",
      "Onboarding Specialist",
      "Boulevard",
      "Customer Success",
      "full-time",
      "USA",
      "Any",
      "The Customer Experience group is responsible for launching, supporting, and strengthening business relationships with Boulevard customers. Playing a critical role in the customer journey, the Onboarding Specialists serve as project managers, guides and partners to their customers, owning the relationship from sale to adoption. *This role is ineligible for residents of CA, NY, and WA*&amp;#8230;",
      "2025-05-06 16:24:24",
      "None",
      "None"
    ),
    (
      117336,
      "117336-developer-evangelist",
      "Developer Evangelist",
      "Twilio",
      "Programming",
      "full-time",
      "Ireland,  UK",
      "Any",
      "This position is needed to help us inspire and equip a global network of millions of developers who will build the future of customer engagement. The Developer Evangelist will define developer relations in the EMEA region, while sustaining a relationship that fuels every developer&amp;#8217;s journey to know, use and love Twilio. The Developer Evangelist will&amp;#8230;",
      "2025-05-06 11:55:02",
      "Npne",
      "None"
    ),
    (
      116718,
      "116718-senior-web-designer-customer-education-2",
      "Sr. Staff Product Designer, Grow &amp;amp; Extend",
      "Webflow",
      "Web &amp; App Design",
      "full-time",
      "Canada,  USA",
      "Senior",
      "We are seeking a Senior Staff Product Designer to join our team and help businesses of all sizes discover, use, and grow with Webflow. You will elevate and launch intuitive experiences that highlight the platform&amp;#8217;s value, enabling seamless adoption of powerful features. Your role involves collaborating across teams to strategize, explore, validate, and build solutions&amp;#8230;",
      "2025-05-06 04:55:46",
      200000,
      220000
    ),
    (
      116056,
      "116056-lead-security-engineer",
      "Lead Security Engineer",
      "Reify Health",
      "Software Engineering",
      "full-time",
      "USA",
      "Any",
      "By joining our team as a Lead Security Engineer, you will become a leading subject matter expert on the security of modern web applications, APIs, and cloud infrastructure. In close collaboration with technical advisors and staff engineers, you will assess the security of new applications, features, partner integrations, data flows, and internal StudyTeam configuration/administration tools. You&amp;#8230;",
      "2025-05-06 04:55:20",
      200000,
      220000
    ),
    (
      116053,
      "116053-educational-support-representative-2",
      "Educational Sales Representative",
      "Varsity Tutors",
      "Sales",
      "full-time",
      "USA",
      "Any",
      "As an Educational Sales Representative, you&amp;#8217;ll leverage your educational background to guide prospective students and families toward personalized learning solutions. This is a SALES position that requires a consultative approach when selling to clients. Success in this role comes from: Conducting meaningful needs assessment conversations with families Applying your teaching/training experience to recommend tailored learning&amp;#8230;",
      "2025-05-06 04:54:22",
      "None",
      "None"
    ),
    (
      75087,
      "75087-sr-group-manager-customer-success-strategic",
      "Clinical Care Navigator",
      "Lyra Health",
      "Customer Success",
      "full-time",
      "USA",
      "Any",
      "As a Clinical Care Navigator,  you’ll be doing the important, meaningful work of managing crises, providing in-the-moment phone support to clients with complex behavioral health issues, ensuring client safety, and connecting clients to high-quality, evidence-based providers and facilities. This position does not involve providing in-person services or therapy but instead focuses on supporting clients in&amp;#8230;",
      "2025-05-06 04:54:11",
      101382,
      209296
    ),
    (
      114408,
      "114408-senior-product-designer-platform-3",
      "Senior Product Designer, Platform",
      "Coinbase",
      "Web &amp; App Design",
      "full-time",
      "USA",
      "Senior",
      "At Coinbase, our mission is to increase economic freedom in the world. It’s a massive, ambitious opportunity that demands the best of us, every day, as we build the emerging onchain platform — and with it, the future global financial system. To achieve our mission, we’re seeking a very specific candidate. We want someone who&amp;#8230;",
      "2025-05-06 04:53:48",
      151500,
      215500
    ),
    (
      94818,
      "94818-senior-data-scientist-10",
      "Senior Data Scientist",
      "Coinbase",
      "Data Science &amp; Analytics",
      "full-time",
      "USA",
      "Senior",
      "To achieve our mission, we’re seeking a very specific candidate. We want someone who is passionate about our mission and who believes in the power of crypto and blockchain technology to update the financial system. We want someone who is eager to leave their mark on the world, who relishes the pressure and privilege of&amp;#8230;",
      "2025-05-06 04:53:39",
      "None",
      "None"
    ),
    (
      112975,
      "112975-software-engineer-6",
      "Full Stack Software Engineer",
      "SugarCRM",
      "Software Engineering",
      "full-time",
      "Romania",
      "Any",
      "From the very beginning, SugarCRM had a unique vision: to offer a different kind of Customer Relationship Management (CRM). We pioneered the first commercial open-source CRM platform, and now, more than two decades later, are on a mission to provide products and services that make the hard things easier for sales, marketing and customer service teams. In&amp;#8230;",
      "2025-05-06 04:52:57",
      134000,
      214000
    ),
    (
      94821,
      "94821-inside-sales-representative-10",
      "Inside Sales Representative",
      "Liberty Mutual",
      "Sales",
      "full-time",
      "USA",
      "Any",
      "The typical starting salary range for this role is determined by a number of factors including skills, experience, education, certifications and location. The full salary range for this role reflects the competitive labor market value for all employees in these positions across the national market and provides an opportunity to progress as employees grow and&amp;#8230;",
      "2025-05-06 04:51:39",
      "None",
      "None"
    ),
    (
      108937,
      "108937-security-software-engineer",
      "Staff Security Software Engineer",
      "Quora",
      "Software Engineering",
      "full-time",
      "Canada,  Costa Rica,  Estonia,  Germany,  Ireland,  Mexico,  Poland,  South Korea,  Thailand,  UK,  USA",
      "Any",
      "Quora’s mission is to grow and share the world’s knowledge. To do so, we have two knowledge sharing products: Quora: a global knowledge sharing platform with over 400M monthly unique visitors, bringing people together to share insights on various topics and providing a unique platform to learn and connect with others. Poe: a platform providing&amp;#8230;",
      "2025-05-06 04:50:30",
      95000,
      106000
    ),
    (
      116032,
      "116032-senior-software-engineer-rust-backend",
      "Senior Software Engineer, Rust (Backend)",
      "Kraken",
      "Software Engineering",
      "full-time",
      "LATAM,  Canada,  Europe,  USA",
      "Senior",
      "Join our Crypto team to help integrate Kraken’s systems with an ever-expanding universe of cryptocurrencies and blockchains. As a member of this team, your focus is elevating our clients&amp;#8217; crypto journey and delivering new and exciting ways to accelerate crypto adoption. Your counterparts will be the hardcore Rust backend engineering teams,  the blockchain maxi who&amp;#8230;",
      "2025-05-06 04:50:00",
      60000,
      75000
    ),
    (
      116030,
      "116030-manager-mid-market-customer-success",
      "Onboarding Manager - Enterprise",
      "Boulevard",
      "Customer Success",
      "full-time",
      "USA",
      "Any",
      "The Customer Experience group is responsible for launching, supporting, and strengthening business relationships with Boulevard’s customers. As an Onboarding Manager, Enterprise, you will lead a team of approximately 5-7 Enterprise Onboarding Specialists (OSs),ensuring the seamless onboarding of our largest, most complex customers. This includes multi-location enterprises, franchises, and private equity-backed organizations that require customized onboarding&amp;#8230;",
      "2025-05-06 04:49:34",
      135000,
      165000
    ),
    (
      116723,
      "116723-senior-data-engineer-4",
      "Sr. Data Engineer",
      "Built Technologies",
      "Data Science &amp; Analytics",
      "full-time",
      "USA",
      "Senior",
      "Built is looking for an experienced Senior Data Engineer to help organize and manage existing data resources, implement new technologies and tooling to grow our business products through our data analysis platform, as well as drive scalable data-sharing practices. You will own data environments, integrate with new technologies, and oversee the development of new processes&amp;#8230;",
      "2025-05-06 04:48:09",
      78000,
      145000
    ),
    (
      117333,
      "117333-staff-product-designer-8",
      "Staff Product Designer",
      "Dropbox",
      "Creative &amp; Design",
      "full-time",
      "Canada,  USA",
      "Any",
      "As a Staff Designer at Organize the Cloud, you will be at the forefront of reimagining design for the next generation of AI-powered products. You will help define the future of our mobile experiences, collaborating across teams to integrate cutting-edge technologies that make our product even more intuitive, intelligent, and powerful. Your role will focus&amp;#8230;",
      "2025-05-06 04:39:22",
      "None",
      "None"
    ),
    (
      117331,
      "117331-customer-success-manager-27",
      "Customer Success Manager",
      "Deel",
      "Customer Success",
      "full-time",
      "EMEA",
      "Any",
      "You’ll be the face and voice of Deel for our clients, both internally and externally. In this dynamic role, you’ll be responsible for building genuine and durable customer relationships while converting those relationships into opportunities for long-term revenue growth. You will serve as our client’s trusted advisor by providing strategic guidance on operational and product-related&amp;#8230;",
      "2025-05-06 04:34:30",
      228000,
      328000
    ),
    (
      117330,
      "117330-ux-designer",
      "UX Designer",
      "UpKeep",
      "Web &amp; App Design",
      "full-time",
      "Brazil",
      "Any",
      "In this role, you are a vital part of what drives the future of our product in collaboration with product and engineering. You will have latitude to improve processes, tools, and the Product Design discipline. You will help shape this function and build the Product Design team. Dig deep on integrating an elegant experience across&amp;#8230;",
      "2025-05-06 04:30:45",
      175100,
      206000
    ),
    (
      117329,
      "117329-manager-product-design-2",
      "Manager, Product Design",
      "1Password",
      "Creative &amp; Design",
      "full-time",
      "Canada,  USA",
      "Any",
      "The Experience, Design &amp;amp; Research department at 1Password exists to explore, research, design and champion the most delightful, clear and useful experience for all our customers, empowering them to be both secure and productive at work and at home. We&amp;#8217;re looking for a Product Design Manager to lead a talented team of designers within our&amp;#8230;",
      "2025-05-06 04:27:23",
      175100,
      206000
    ),
    (
      117325,
      "117325-global-benefits-specialist",
      "Global Benefits Specialist",
      "StackAdapt",
      "HR &amp; Recruiting",
      "full-time",
      "UK",
      "Any",
      "As the Global Benefits Specialist, you will be responsible for administering and enhancing our global benefits. This includes company-wide group benefits plans like health and welfare, global wellness programs, and time off policies. Reporting to the Senior Global Benefits Manager. You’ll partner with internal stakeholders to deliver a holistic benefits package aligned with our Total&amp;#8230;",
      "2025-05-06 04:23:36",
      55000,
      75000
    ),
    (
      116030,
      "116030-manager-mid-market-customer-success",
      "Onboarding Manager - Enterprise",
      "Boulevard",
      "Customer Success",
      "full-time",
      "USA",
      "Any",
      "The Customer Experience group is responsible for launching, supporting, and strengthening business relationships with Boulevard’s customers. As an Onboarding Manager, Enterprise, you will lead a team of approximately 5-7 Enterprise Onboarding Specialists (OSs),ensuring the seamless onboarding of our largest, most complex customers. This includes multi-location enterprises, franchises, and private equity-backed organizations that require customized onboarding&amp;#8230;",
      "2025-05-06 04:49:34",
      155656,
      277387
    ),
    (
      116723,
      "116723-senior-data-engineer-4",
      "Sr. Data Engineer",
      "Built Technologies",
      "Data Science &amp; Analytics",
      "full-time",
      "USA",
      "Senior",
      "Built is looking for an experienced Senior Data Engineer to help organize and manage existing data resources, implement new technologies and tooling to grow our business products through our data analysis platform, as well as drive scalable data-sharing practices. You will own data environments, integrate with new technologies, and oversee the development of new processes&amp;#8230;",
      "2025-05-06 04:48:09",
      135000,
      203000
    ),
    (
      117333,
      "117333-staff-product-designer-8",
      "Staff Product Designer",
      "Dropbox",
      "Creative &amp; Design",
      "full-time",
      "Canada,  USA",
      "Any",
      "As a Staff Designer at Organize the Cloud, you will be at the forefront of reimagining design for the next generation of AI-powered products. You will help define the future of our mobile experiences, collaborating across teams to integrate cutting-edge technologies that make our product even more intuitive, intelligent, and powerful. Your role will focus&amp;#8230;",
      "2025-05-06 04:39:22",
      77280,
      110400
    ),
    (
      117331,
      "117331-customer-success-manager-27",
      "Customer Success Manager",
      "Deel",
      "Customer Success",
      "full-time",
      "EMEA",
      "Any",
      "You’ll be the face and voice of Deel for our clients, both internally and externally. In this dynamic role, you’ll be responsible for building genuine and durable customer relationships while converting those relationships into opportunities for long-term revenue growth. You will serve as our client’s trusted advisor by providing strategic guidance on operational and product-related&amp;#8230;",
      "2025-05-06 04:34:30",
      140000,
      170000
    ),
    (
      117330,
      "117330-ux-designer",
      "UX Designer",
      "UpKeep",
      "Web &amp; App Design",
      "full-time",
      "Brazil",
      "Any",
      "In this role, you are a vital part of what drives the future of our product in collaboration with product and engineering. You will have latitude to improve processes, tools, and the Product Design discipline. You will help shape this function and build the Product Design team. Dig deep on integrating an elegant experience across&amp;#8230;",
      "2025-05-06 04:30:45",
      178500,
      241500
    ),
    (
      117329,
      "117329-manager-product-design-2",
      "Manager, Product Design",
      "1Password",
      "Creative &amp; Design",
      "full-time",
      "Canada,  USA",
      "Any",
      "The Experience, Design &amp;amp; Research department at 1Password exists to explore, research, design and champion the most delightful, clear and useful experience for all our customers, empowering them to be both secure and productive at work and at home. We&amp;#8217;re looking for a Product Design Manager to lead a talented team of designers within our&amp;#8230;",
      "2025-05-06 04:27:23",
      173000,
      233000
    ),
    (
      117325,
      "117325-global-benefits-specialist",
      "Global Benefits Specialist",
      "StackAdapt",
      "HR &amp; Recruiting",
      "full-time",
      "UK",
      "Any",
      "As the Global Benefits Specialist, you will be responsible for administering and enhancing our global benefits. This includes company-wide group benefits plans like health and welfare, global wellness programs, and time off policies. Reporting to the Senior Global Benefits Manager. You’ll partner with internal stakeholders to deliver a holistic benefits package aligned with our Total&amp;#8230;",
      "2025-05-06 04:23:36",
      "None",
      "None"
    ),
    (
      117323,
      "117323-staff-data-engineer",
      "Staff Data Engineer",
      "1Password",
      "Data Science &amp; Analytics",
      "full-time",
      "Canada,  USA",
      "Any",
      "As a Staff Data Engineer, you will be leading the architecture, design and development of data pipelines and services to enable data-driven decision-making, deliver business intelligence, machine learning, experimentation and company-wide data strategy. This is a remote opportunity within Canada and the US. What we&amp;#8217;re looking for: Minimum of 8+ years of professional software engineering&amp;#8230;",
      "2025-05-06 04:20:29",
      177000,
      239000
    )
    
""")
con.commit()
print("-->Every companies that are hiring software engineering and allows to work anywhere")
for row in cur.execute("SELECT companyName FROM JobAppli WHERE jobIndustry LIKE '%Software Engineering%' AND jobGeo LIKE '%Any%'"):
  print(row[0])
  
  
print("-->Average of max annual salary that software engineer get")
for row in cur.execute("SELECT AVG(annualSalaryMax) FROM JobAppli WHERE jobIndustry LIKE '%Software Engineering%' AND annualSalaryMax != 'None'"):
  print(row[0])


print("-->Every job industry that only get max annual salary more than 150000")
for row in cur.execute("SELECT DISTINCT jobIndustry FROM JobAppli WHERE jobIndustry NOT IN (SELECT jobIndustry FROM JobAppli WHERE annualSalaryMax <= 150000)"):
  print(row[0])
  
  
print("-->Every full-time jobs that offer a senior level job")
company = []
headers = ["Company", "Job title"]
for row in cur.execute("SELECT DISTINCT companyName, jobTitle FROM JobAppli WHERE jobType = 'full-time' AND jobLevel = 'Senior'"):
  company.append(row)
company_p = pd.DataFrame(company, columns = headers)
print(company_p)


print("-->Differences of annual salary of every companies")
diff = []
headers = ["Company", "Job title", "Difference of salary"]
for row in cur.execute("SELECT companyName, jobTitle, annualSalaryMax-annualSalaryMin FROM JobAppli WHERE annualSalaryMax != 'None'"):
  diff.append(row)
diff_p = pd.DataFrame(diff, columns = headers)
print(diff_p)

print("-->Top 5 Job industries that earn the greatest amount of max annual salary")
top = []
headers = ["Company", "Job industry", "Max annual salary"]
i = 5
for row in cur.execute("SELECT companyName, jobIndustry, annualSalaryMax FROM JobAppli AS J1 WHERE J1.annualSalaryMax <> 'None' AND NOT EXISTS (SELECT * FROM JobAppli AS J2 WHERE J2.annualSalaryMax != 'None' AND J2.annualSalaryMax > J1.annualSalaryMax AND J2.jobIndustry = J1.jobIndustry) ORDER BY annualSalaryMax DESC"):
  top.append(row)
  i = i-1
  if i == 0:
    break
top_p = pd.DataFrame(top, columns = headers)
print(top_p)

con.close()