from vkwave.types.responses import *

from ._category import Category


class Fave(Category):
    async def add_article(self, url: str = None,) -> BaseBoolResponse:
        """
        :param url:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addArticle", params)
        result = BaseBoolResponse(**raw_result)
        return result

    async def add_link(self, link: str = None,) -> OkResponse:
        """
        :param link: - Link URL.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addLink", params)
        result = OkResponse(**raw_result)
        return result

    async def add_page(
        self, user_id: typing.Optional[int] = None, group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addPage", params)
        result = OkResponse(**raw_result)
        return result

    async def add_post(
        self, owner_id: int = None, id: int = None, access_key: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addPost", params)
        result = OkResponse(**raw_result)
        return result

    async def add_product(
        self, owner_id: int = None, id: int = None, access_key: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addProduct", params)
        result = OkResponse(**raw_result)
        return result

    async def add_tag(self, name: typing.Optional[str] = None,) -> FaveAddTagResponse:
        """
        :param name:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addTag", params)
        result = FaveAddTagResponse(**raw_result)
        return result

    async def add_video(
        self, owner_id: int = None, id: int = None, access_key: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :param access_key:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("addVideo", params)
        result = OkResponse(**raw_result)
        return result

    async def edit_tag(self, id: int = None, name: str = None,) -> OkResponse:
        """
        :param id:
        :param name:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("editTag", params)
        result = OkResponse(**raw_result)
        return result

    async def get(
        self,
        extended: typing.Optional[bool] = None,
        item_type: typing.Optional[str] = None,
        tag_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        is_from_snackbar: typing.Optional[bool] = None,
    ) -> FaveGetResponse:
        """
        :param extended: - '1' — to return additional 'wall', 'profiles', and 'groups' fields. By default: '0'.
        :param item_type:
        :param tag_id: - Tag ID.
        :param offset: - Offset needed to return a specific subset of users.
        :param count: - Number of users to return.
        :param fields:
        :param is_from_snackbar:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = FaveGetResponse(**raw_result)
        return result

    async def get_pages(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        tag_id: typing.Optional[int] = None,
    ) -> FaveGetPagesResponse:
        """
        :param offset:
        :param count:
        :param type:
        :param fields:
        :param tag_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getPages", params)
        result = FaveGetPagesResponse(**raw_result)
        return result

    async def get_tags(self,) -> FaveGetTagsResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getTags", params)
        result = FaveGetTagsResponse(**raw_result)
        return result

    async def mark_seen(self,) -> BaseBoolResponse:
        """
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("markSeen", params)
        result = BaseBoolResponse(**raw_result)
        return result

    async def remove_article(
        self, owner_id: int = None, article_id: int = None,
    ) -> BaseBoolResponse:
        """
        :param owner_id:
        :param article_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeArticle", params)
        result = BaseBoolResponse(**raw_result)
        return result

    async def remove_link(
        self, link_id: typing.Optional[str] = None, link: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param link_id: - Link ID (can be obtained by [vk.com/dev/faves.getLinks|faves.getLinks] method).
        :param link: - Link URL
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeLink", params)
        result = OkResponse(**raw_result)
        return result

    async def remove_page(
        self, user_id: typing.Optional[int] = None, group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removePage", params)
        result = OkResponse(**raw_result)
        return result

    async def remove_post(self, owner_id: int = None, id: int = None,) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removePost", params)
        result = OkResponse(**raw_result)
        return result

    async def remove_product(self, owner_id: int = None, id: int = None,) -> OkResponse:
        """
        :param owner_id:
        :param id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeProduct", params)
        result = OkResponse(**raw_result)
        return result

    async def remove_tag(self, id: int = None,) -> OkResponse:
        """
        :param id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("removeTag", params)
        result = OkResponse(**raw_result)
        return result

    async def reorder_tags(self, ids: typing.List[int] = None,) -> OkResponse:
        """
        :param ids:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("reorderTags", params)
        result = OkResponse(**raw_result)
        return result

    async def set_page_tags(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :param tag_ids:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setPageTags", params)
        result = OkResponse(**raw_result)
        return result

    async def set_tags(
        self,
        item_type: typing.Optional[str] = None,
        item_owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        tag_ids: typing.Optional[typing.List[int]] = None,
        link_id: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
    ) -> OkResponse:
        """
        :param item_type:
        :param item_owner_id:
        :param item_id:
        :param tag_ids:
        :param link_id:
        :param link_url:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("setTags", params)
        result = OkResponse(**raw_result)
        return result

    async def track_page_interaction(
        self, user_id: typing.Optional[int] = None, group_id: typing.Optional[int] = None,
    ) -> OkResponse:
        """
        :param user_id:
        :param group_id:
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("trackPageInteraction", params)
        result = OkResponse(**raw_result)
        return result
