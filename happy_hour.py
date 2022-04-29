import random

skill = ["SQL",
         "Python",
         "R",
         "Git"]

website = ["datacamp",
           "coursera",
           "onemonth",
           "udemy"]

random_skill = random.choice(skill)
random_website = random.choice(website)

print(f"How about learning {random_skill} from {random_website} website?")