from bcr_api.bwproject import BWProject, BWUser
from bcr_api.bwresources import BWQueries, BWGroups, BWAuthorLists, BWSiteLists, BWLocationLists, BWTags, BWCategories, BWRules, BWMentions, BWSignals
import datetime

BWUser(username="seesuite@uga.edu", password="SEESuite1!", token_path="tokens.txt")

YOUR_ACCOUNT = "seesuite@uga.edu"
YOUR_PROJECT = "1998295055"

project = BWProject(username=YOUR_ACCOUNT, project=YOUR_PROJECT)
queries = BWQueries(project)

today = (datetime.date.today() + datetime.timedelta(days=1)).isoformat() + "T05:00:00"
start = (datetime.date.today() - datetime.timedelta(days=29)).isoformat() + "T05:00:00"

filtered = queries.get_mentions(name = "Himelboim-COVID-19 Vaccine ", 
                                startDate = start, 
                                endDate = today, 
                                pageType = "twitter",
                                twitterRetweetsMin = 20)