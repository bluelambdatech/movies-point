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

        url = f"{base_url}?jql=project={project_key}"

        return cls(url=url, user=user_name, token=token)

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

        # print(self.client.projects())
        # for prj in self.client.projects():
        #     print(type(prj.key))

        # get an issue to update
        # issue = self.client.issue("MOVIES-1")
        # print(issue)
        #
        # self.client.add_comment(issue, "Comment text")



moviejira = JiraAPI.create_conn()


