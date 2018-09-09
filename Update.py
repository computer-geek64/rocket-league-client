# Update.py
# Ashish D'Souza
# September 8th, 2018

import os
import Git


repository_name = os.getcwd().split("/win")[0]
Git.fetch(repository_name)
if not Git.is_up_to_date(repository_name):
    Git.pull(repository_name)
