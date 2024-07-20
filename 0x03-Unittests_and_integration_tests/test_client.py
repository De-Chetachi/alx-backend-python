#!/usr/bin/env python3
'''test for client module'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from typing import List
import client
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest.TestCase):
    '''test class for githuborgclient'''

    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, get_json):
        '''test that GithubOrgClient.org returns the right result'''
        client_ = client.GithubOrgClient(org)
        self.assertEqual(client_.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org}"
        get_json.assert_called_once_with(url)


    def test_public_repos_url(self, org="google"):
        '''test for GithubOrgClient._public_repos_url.'''

        client_ = client.GithubOrgClient(org)
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_org.return_value = payload
        self.assertEqual(client_._public_repos_url, payload.get("repos_url"))



    @patch("client.get_json")
    def test_public_repos(self, mock_get_json, org="google"):
        '''unittest for TestGithubOrgClient.test_public_repos'''
        
        payload = [{"name": "repo_1"}, {"name": "repo_2"}]
        mock_get_json.return_value = payload

        with patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock) as mock_org_repo:
            mock_org_repo.return_value = "https://api.github.com/orgs/google/repos"
            client_1 = client.GithubOrgClient(org)
            self.assertEqual(client_1.public_repos(), ["repo_1", "repo_2"])
            mock_get_json.assert_called_once()
            mock_org_repo.assert_called_once()


    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_keys, expected):
        '''unittest for GithubOrgClient.has_license'''
        client_2 = client.GithubOrgClient("google")
        self.assertEqual(client_2.has_license(repo, license_keys), expected)



@parameterized_class((org_payload, repos_payload, expected_repos, apache2_repos), [


    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''integration test for public_repos'''
    
    @classmethod
    def setUpClass(cls):
        '''set up done before running tests'''



    @classmethod
    def tearDownClass(cls):
        '''called after test in a test class a run'''




if __name__ == "__main__":
    unittest.main()
