from vkwave.types.responses import *

from ._category import Category


class Account(Category):
    async def ban(self, owner_id: typing.Optional[int] = None, ) -> OkResponse:
        """
        :param owner_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("ban", params)
        result = OkResponse(**raw_result)
        return result

    async def change_password(
            self,
            restore_sid: typing.Optional[str] = None,
            change_password_hash: typing.Optional[str] = None,
            old_password: typing.Optional[str] = None,
            new_password: str = None,
    ) -> AccountChangePasswordResponse:
        """
        :param restore_sid: - Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: - Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: - Current user password.
        :param new_password: - New password that will be set as a current
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("changePassword", params)
        result = AccountChangePasswordResponse(**raw_result)
        return result

    async def get_active_offers(
            self, offset: typing.Optional[int] = None, count: typing.Optional[int] = None,
    ) -> AccountGetActiveOffersResponse:
        """
        :param offset:
        :param count: - Number of results to return.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getActiveOffers", params)
        result = AccountGetActiveOffersResponse(**raw_result)
        return result

    async def get_app_permissions(
            self, user_id: int = None,
    ) -> AccountGetAppPermissionsResponse:
        """
        :param user_id: - User ID whose settings information shall be got. By default: current user.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getAppPermissions", params)
        result = AccountGetAppPermissionsResponse(**raw_result)
        return result

    async def get_banned(
            self, offset: typing.Optional[int] = None, count: typing.Optional[int] = None,
    ) -> AccountGetBannedResponse:
        """
        :param offset: - Offset needed to return a specific subset of results.
        :param count: - Number of results to return.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getBanned", params)
        result = AccountGetBannedResponse(**raw_result)
        return result

    async def get_counters(
            self, filter: typing.Optional[typing.List[str]] = None,
    ) -> AccountGetCountersResponse:
        """
        :param filter: - Counters to be returned.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getCounters", params)
        result = AccountGetCountersResponse(**raw_result)
        return result

    async def get_info(
            self, fields: typing.Optional[typing.List[str]] = None,
    ) -> AccountGetInfoResponse:
        """
        :param fields: - Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getInfo", params)
        result = AccountGetInfoResponse(**raw_result)
        return result

    async def get_profile_info(self, ) -> AccountGetProfileInfoResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getProfileInfo", params)
        result = AccountGetProfileInfoResponse(**raw_result)
        return result

    async def get_push_settings(
            self, device_id: typing.Optional[str] = None,
    ) -> AccountGetPushSettingsResponse:
        """
        :param device_id: - Unique device ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getPushSettings", params)
        result = AccountGetPushSettingsResponse(**raw_result)
        return result

    async def register_device(
            self,
            token: str = None,
            device_model: typing.Optional[str] = None,
            device_year: typing.Optional[int] = None,
            device_id: str = None,
            system_version: typing.Optional[str] = None,
            settings: typing.Optional[str] = None,
            sandbox: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param token: - Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: - String name of device model.
        :param device_year: - Device year.
        :param device_id: - Unique device ID.
        :param system_version: - String version of device operating system.
        :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("registerDevice", params)
        result = OkResponse(**raw_result)
        return result

    async def save_profile_info(
            self,
            first_name: typing.Optional[str] = None,
            last_name: typing.Optional[str] = None,
            maiden_name: typing.Optional[str] = None,
            screen_name: typing.Optional[str] = None,
            cancel_request_id: typing.Optional[int] = None,
            sex: typing.Optional[int] = None,
            relation: typing.Optional[int] = None,
            relation_partner_id: typing.Optional[int] = None,
            bdate: typing.Optional[str] = None,
            bdate_visibility: typing.Optional[int] = None,
            home_town: typing.Optional[str] = None,
            country_id: typing.Optional[int] = None,
            city_id: typing.Optional[int] = None,
            status: typing.Optional[str] = None,
    ) -> AccountSaveProfileInfoResponse:
        """
        :param first_name: - User first name.
        :param last_name: - User last name.
        :param maiden_name: - User maiden name (female only)
        :param screen_name: - User screen name.
        :param cancel_request_id: - ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: - User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: - User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: - ID of the relationship partner.
        :param bdate: - User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: - Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: - User home town.
        :param country_id: - User country.
        :param city_id: - User city.
        :param status: - Status text.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("saveProfileInfo", params)
        result = AccountSaveProfileInfoResponse(**raw_result)
        return result

    async def set_info(
            self, name: typing.Optional[str] = None, value: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param name: - Setting name.
        :param value: - Setting value.
        :return:
        """

        params = {}
        for key, value_ in locals().items():
            if key not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value = ",".join(str(item) for item in value_)
                params[key] = value_

        raw_result = await self.api_request("setInfo", params)
        result = OkResponse(**raw_result)
        return result

    async def set_name_in_menu(
            self, user_id: int = None, name: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param user_id: - User ID.
        :param name: - Application screen name.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setNameInMenu", params)
        result = OkResponse(**raw_result)
        return result

    async def set_offline(self, ) -> OkResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setOffline", params)
        result = OkResponse(**raw_result)
        return result

    async def set_online(self, voip: typing.Optional[bool] = None, ) -> OkResponse:
        """
        :param voip: - '1' if videocalls are available for current device.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setOnline", params)
        result = OkResponse(**raw_result)
        return result

    async def set_push_settings(
            self,
            device_id: str = None,
            settings: typing.Optional[str] = None,
            key: typing.Optional[str] = None,
            value: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param device_id: - Unique device ID.
        :param settings: - Push settings in a [vk.com/dev/push_settings|special format].
        :param key: - Notification key.
        :param value: - New value for the key in a [vk.com/dev/push_settings|special format].
        :return:
        """

        params = {}
        for key_, value_ in locals().items():
            if key_ not in ["self", "params"] and value_ is not None:
                if isinstance(value_, list):
                    value_ = ",".join(str(item) for item in value_)
                params[key_] = value_

        raw_result = await self.api_request("setPushSettings", params)
        result = OkResponse(**raw_result)
        return result

    async def set_silence_mode(
            self,
            device_id: typing.Optional[str] = None,
            time: typing.Optional[int] = None,
            peer_id: typing.Optional[int] = None,
            sound: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param device_id: - Unique device ID.
        :param time: - Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: - '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setSilenceMode", params)
        result = OkResponse(**raw_result)
        return result

    async def unban(self, owner_id: typing.Optional[int] = None, ) -> OkResponse:
        """
        :param owner_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unban", params)
        result = OkResponse(**raw_result)
        return result

    async def unregister_device(
            self,
            device_id: typing.Optional[str] = None,
            sandbox: typing.Optional[bool] = None,
    ) -> OkResponse:
        """
        :param device_id: - Unique device ID.
        :param sandbox:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("unregisterDevice", params)
        result = OkResponse(**raw_result)
        return result
