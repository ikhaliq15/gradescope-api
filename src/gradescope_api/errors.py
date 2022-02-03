from msilib.schema import Error
from requests import Response
import json


class GradescopeAPIError(Error):
    pass


class AuthError(GradescopeAPIError):
    pass


class RequestError(GradescopeAPIError):
    pass


def check_response(response: Response, error: str):
    if not response.ok:
        raise RequestError(
            "An error occurred in a request to Gradescope servers. Details: "
            + "\n"
            + "Status Code: "
            + str(response.status_code)
            + "\n"
            + "Error: "
            + str(error)
            + "\n"
            "Request: " + json.dumps(vars(response.request)) + "\n" + "Response: " + str(response.content)
        )
