from jira import JIRA
import requests

import os

from dotenv import load_dotenv

load_dotenv()


project_key = "MOVIES"


class JiraAPI:
    @classmethod
    def create_conn(cls):
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        base_url = os.getenv("jira_base_url")
        token = os.getenv("jira_token")
        user_name = os.getenv("jira_user_name")

        return cls(url=base_url, user=user_name, token=token)

    def __init__(self, url, user, token):
        self.client = JIRA(url, basic_auth=(user, token))

        #print(self.client.search_issues("project=MOVIES"))
        #print(self.client.createmeta("MOVIES"))

        data = {
                "fields":
                {
                    "project":
                    {
                        "key": "MOVIES"
                    },
                    "parent":
                    {
                        "key": "TEST-101"
                    },
                    "summary": "Sub-task of TEST-101",
                    "description": "Don't forget to do this too.",
                    "issuetype":
                    {
                        "id": "5"
                    }
                }
            }

    def get_projects(self):
        projects_list = []
        # print(self.client.projects())
        for prj in self.client.projects():
            projects_list.append(prj.key)

        return projects_list

    def get_issue(self, issueName):
        # get an issue to update
        # issue = self.client.issue("MOVIES-1")
        # print(issue)
        #
        pass

    def create_issue(self, name, email):
        pass

    def add_comment(self, issueName, comment, description):
        self.client.add_comment(issueName, comment)
        # print(self.client.get_all_custom_fields())
        #print(self.client.issue("MOVIES-1").id)

    def add_description(self):
        pass



moviejira = JiraAPI.create_conn()

moviejira.add_comment("MOVIES-3", "AM trying to take Nene thru what we did", "Nene")

