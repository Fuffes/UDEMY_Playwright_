import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext, expect
from typing import Generator
from configuration import GITHUB_TOKEN, GITHUB_PEPO, GITHUB_USER


@pytest.fixture(scope = "session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept" : "application/vnd.github.v3+json",
        "Authorization" : f"token {GITHUB_TOKEN}",
    }

    request_contex = playwright.request.new_context(
        base_url="https://api.github/com", extra_http_headers=headers
    )
    yield request_contex
    request_contex.dispose()



@pytest.fixture(scope="session", autouse=True)
def create_test_repo(
    api_request_context: APIRequestContext
)-> Generator[None, None, None]:
    new_repo = api_request_context.post("/user/repos", data={"name": {GITHUB_PEPO}})
    assert new_repo.ok
    yield 
    delete_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_PEPO}")
    assert delete_repo.ok



def test_bug_report(api_request_context) -> None:
    data = {"title": "[Bug] bug_1", 
            "body" : "Bug description",
            }
    new_bug = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_PEPO}/issues", data=data)
    assert new_bug.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_PEPO}/issues")
    assert issues.ok

    issues_req = issues.json()
    issue = list(filter(lambda issue: issue["title"] == data["title"], issues_req))[0]
    assert issue
    assert issue["boby"] == data["body"]




def test_feature(api_request_context: APIRequestContext) -> None:
    data = {"title": "[Feature] req 1 ", 
            "body" : "Feature description",
            }
    new_issue = api_request_context.post(f"/repos/{GITHUB_USER}/{GITHUB_PEPO}/issues", data=data)
    assert new_issue.ok

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_PEPO}/issues")
    assert issues.ok

    issues_req = issues.json()
    issue = list(filter(lambda issue: issue["title"] == data["title"], issues_req))[0]
    assert issue
    assert issue["boby"] == data["body"]
