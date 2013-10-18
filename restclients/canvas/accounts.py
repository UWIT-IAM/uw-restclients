from restclients.canvas import Canvas
from restclients.dao import Canvas_DAO
from restclients.models.canvas import Account
from restclients.exceptions import DataFailureException
import json


class Accounts(Canvas):
    def get_account(self, account_id):
        """
        Return account resource for given canvas account id.

        https://canvas.instructure.com/doc/api/accounts.html#method.accounts.show
        """
        url = "/api/v1/accounts/%s" % account_id
        return self._account_from_json(self._get_resource(url))

    def get_account_by_canvas_id(self, canvas_id):
        """
        Alias method for get_account().
        """
        return self.get_account(canvas_id)

    def get_account_by_sis_id(self, sis_id):
        """
        Return account resource for given sis id.
        """
        return self.get_account(self._sis_id(sis_id))

    def get_sub_accounts(self, account_id, params):
        """
        Return list of subaccounts within the account with the passed canvas id.

        https://canvas.instructure.com/doc/api/accounts.html#method.accounts.sub_accounts
        """
        params = self._pagination(params)
        url = "/api/v1/accounts/%s/sub_accounts%s" % (account_id,
                                                      self._params(params))

        accounts = []
        for datum in self._get_resource(url):
            accounts.append(self._account_from_json(datum))

        return accounts

    def get_sub_accounts_by_canvas_id(self, canvas_id):
        """
        Alias method for get_sub_accounts().
        """
        return self.get_sub_accounts(canvas_id, params={})

    def get_sub_accounts_by_sis_id(self, sis_id):
        """
        Return list of subaccounts within the account with the passed sis id.
        """
        return self.get_sub_accounts(self._sis_id(sis_id), params={})

    def get_all_sub_accounts_by_canvas_id(self, canvas_id):
        """
        Return a recursive list of subaccounts within the account with the passed canvas id.
        """
        return self.get_sub_accounts(canvas_id,
                                     params={"recursive": "true"})

    def get_all_sub_accounts_by_sis_id(self, sis_id):
        """
        Return a recursive list of subaccounts within the account with the passed sis id.
        """
        return self.get_sub_accounts(self._sis_id(sis_id),
                                     params={"recursive": "true"})

    def update_account(self, account_id, resource):
        """
        Update account with the passed canvas id, with given account resource.

        https://canvas.instructure.com/doc/api/accounts.html#method.accounts.update
        """
        url = "/api/v1/accounts/%s" % account_id
        body = json.dumps(resource)

        dao = Canvas_DAO()
        response = dao.putURL(url, {"Content-Type": "application/json"}, body)

        if not (response.status == 200 or response.status == 204):
            raise DataFailureException(url, response.status, response.data)

        return self._account_from_json(response.data)

    def update_account_by_canvas_id(self, canvas_id, resource):
        """
        Alias method for update_account()
        """
        return self.update_account(canvas_id, resource)

    def update_account_by_sis_id(self, sis_id, resource):
        """
        Update account with the passed sis id.
        """
        return self.update_account(self._sis_id(sis_id), resource)

    def _account_from_json(self, data):
        account = Account()
        account.account_id = data["id"]
        account.sis_account_id = data["sis_account_id"]
        account.name = data["name"]
        account.parent_account_id = data["parent_account_id"]
        account.root_account_id = data["root_account_id"]
        return account
