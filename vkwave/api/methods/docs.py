from vkwave.types.responses import *

from ._category import Category


class Docs(Category):
    async def add(
            self,
            owner_id: int = None,
            doc_id: int = None,
            access_key: typing.Optional[str] = None,
    ) -> DocsAddResponse:
        """
        :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :param access_key: - Access key. This parameter is required if 'access_key' was returned with the document's data.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("add", params)
        result = DocsAddResponse(**raw_result)
        return result

    async def delete(self, owner_id: int = None, doc_id: int = None, ) -> OkResponse:
        """
        :param owner_id: - ID of the user or community that owns the document. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("delete", params)
        result = OkResponse(**raw_result)
        return result

    async def edit(
            self,
            owner_id: int = None,
            doc_id: int = None,
            title: typing.Optional[str] = None,
            tags: typing.Optional[typing.List[str]] = None,
    ) -> OkResponse:
        """
        :param owner_id: - User ID or community ID. Use a negative value to designate a community ID.
        :param doc_id: - Document ID.
        :param title: - Document title.
        :param tags: - Document tags.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("edit", params)
        result = OkResponse(**raw_result)
        return result

    async def get(
            self,
            count: typing.Optional[int] = None,
            offset: typing.Optional[int] = None,
            type: typing.Optional[int] = None,
            owner_id: typing.Optional[int] = None,
    ) -> DocsGetResponse:
        """
        :param count: - Number of documents to return. By default, all documents.
        :param offset: - Offset needed to return a specific subset of documents.
        :param type:
        :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("get", params)
        result = DocsGetResponse(**raw_result)
        return result

    async def get_by_id(self, docs: typing.List[str] = None, ) -> DocsGetByIdResponse:
        """
        :param docs: - Document IDs. Example: , "66748_91488,66748_91455",
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getById", params)
        result = DocsGetByIdResponse(**raw_result)
        return result

    async def get_messages_upload_server(
            self, type: typing.Optional[str] = None, peer_id: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param type: - Document type.
        :param peer_id: - Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getMessagesUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def get_types(self, owner_id: int = None, ) -> DocsGetTypesResponse:
        """
        :param owner_id: - ID of the user or community that owns the documents. Use a negative value to designate a community ID.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getTypes", params)
        result = DocsGetTypesResponse(**raw_result)
        return result

    async def get_upload_server(
            self, group_id: typing.Optional[int] = None,
    ) -> DocsGetUploadServer:
        """
        :param group_id: - Community ID (if the document will be uploaded to the community).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getUploadServer", params)
        result = DocsGetUploadServer(**raw_result)
        return result

    async def get_wall_upload_server(
            self, group_id: typing.Optional[int] = None,
    ) -> BaseGetUploadServerResponse:
        """
        :param group_id: - Community ID (if the document will be uploaded to the community).
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("getWallUploadServer", params)
        result = BaseGetUploadServerResponse(**raw_result)
        return result

    async def save(
            self,
            file: str = None,
            title: typing.Optional[str] = None,
            tags: typing.Optional[str] = None,
    ) -> DocsSaveResponse:
        """
        :param file: - This parameter is returned when the file is [vk.com/dev/upload_files_2|uploaded to the server].
        :param title: - Document title.
        :param tags: - Document tags.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("save", params)
        result = DocsSaveResponse(**raw_result)
        return result

    async def search(
            self,
            q: str = None,
            search_own: typing.Optional[bool] = None,
            count: typing.Optional[int] = None,
            offset: typing.Optional[int] = None,
    ) -> DocsSearchResponse:
        """
        :param q: - Search query string.
        :param search_own:
        :param count: - Number of results to return.
        :param offset: - Offset needed to return a specific subset of results.
        :return:
        """

        params = {}
        for key, value in locals().items():
            if key not in ["self", "params"] and value is not None:
                if isinstance(value, list):
                    value = ",".join(str(item) for item in value)
                params[key] = value

        raw_result = await self.api_request("search", params)
        result = DocsSearchResponse(**raw_result)
        return result
