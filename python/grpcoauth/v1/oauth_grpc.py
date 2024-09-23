# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpcoauth/v1/oauth.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import grpcoauth.v1.enums_pb2
import google.protobuf.empty_pb2
import google.api.annotations_pb2
import grpcoauth.v1.oauth_pb2


class OauthServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetOauthAppTokenInfo(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoRequest, grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOauthAppUser(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetOauthAppUserRequest, grpcoauth.v1.oauth_pb2.GetOauthAppUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOauthAppUserList(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetOauthAppUserListRequest, grpcoauth.v1.oauth_pb2.GetOauthAppUserListResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateOauthAdminApp(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.CreateOauthAdminAppRequest, grpcoauth.v1.oauth_pb2.CreateOauthAdminAppResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateOauthUserApp(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.CreateOauthUserAppRequest, grpcoauth.v1.oauth_pb2.CreateOauthUserAppResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAuthorizeCode(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetAuthorizeCodeRequest, grpcoauth.v1.oauth_pb2.GetAuthorizeCodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetToken(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetTokenRequest, grpcoauth.v1.oauth_pb2.GetTokenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAccessTokenInfo(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.GetAccessTokenInfoRequest, grpcoauth.v1.oauth_pb2.GetAccessTokenInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAuthorizeUrl(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, grpcoauth.v1.oauth_pb2.GetAuthorizeUrlResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpcoauth.v1.OauthService/GetOauthAppTokenInfo': grpclib.const.Handler(
                self.GetOauthAppTokenInfo,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoRequest,
                grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoResponse,
            ),
            '/grpcoauth.v1.OauthService/GetOauthAppUser': grpclib.const.Handler(
                self.GetOauthAppUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetOauthAppUserRequest,
                grpcoauth.v1.oauth_pb2.GetOauthAppUserResponse,
            ),
            '/grpcoauth.v1.OauthService/GetOauthAppUserList': grpclib.const.Handler(
                self.GetOauthAppUserList,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetOauthAppUserListRequest,
                grpcoauth.v1.oauth_pb2.GetOauthAppUserListResponse,
            ),
            '/grpcoauth.v1.OauthService/CreateOauthAdminApp': grpclib.const.Handler(
                self.CreateOauthAdminApp,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.CreateOauthAdminAppRequest,
                grpcoauth.v1.oauth_pb2.CreateOauthAdminAppResponse,
            ),
            '/grpcoauth.v1.OauthService/CreateOauthUserApp': grpclib.const.Handler(
                self.CreateOauthUserApp,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.CreateOauthUserAppRequest,
                grpcoauth.v1.oauth_pb2.CreateOauthUserAppResponse,
            ),
            '/grpcoauth.v1.OauthService/GetAuthorizeCode': grpclib.const.Handler(
                self.GetAuthorizeCode,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetAuthorizeCodeRequest,
                grpcoauth.v1.oauth_pb2.GetAuthorizeCodeResponse,
            ),
            '/grpcoauth.v1.OauthService/GetToken': grpclib.const.Handler(
                self.GetToken,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetTokenRequest,
                grpcoauth.v1.oauth_pb2.GetTokenResponse,
            ),
            '/grpcoauth.v1.OauthService/GetAccessTokenInfo': grpclib.const.Handler(
                self.GetAccessTokenInfo,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.GetAccessTokenInfoRequest,
                grpcoauth.v1.oauth_pb2.GetAccessTokenInfoResponse,
            ),
            '/grpcoauth.v1.OauthService/GetAuthorizeUrl': grpclib.const.Handler(
                self.GetAuthorizeUrl,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                grpcoauth.v1.oauth_pb2.GetAuthorizeUrlResponse,
            ),
        }


class OauthServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetOauthAppTokenInfo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetOauthAppTokenInfo',
            grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoRequest,
            grpcoauth.v1.oauth_pb2.GetOauthAppTokenInfoResponse,
        )
        self.GetOauthAppUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetOauthAppUser',
            grpcoauth.v1.oauth_pb2.GetOauthAppUserRequest,
            grpcoauth.v1.oauth_pb2.GetOauthAppUserResponse,
        )
        self.GetOauthAppUserList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetOauthAppUserList',
            grpcoauth.v1.oauth_pb2.GetOauthAppUserListRequest,
            grpcoauth.v1.oauth_pb2.GetOauthAppUserListResponse,
        )
        self.CreateOauthAdminApp = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/CreateOauthAdminApp',
            grpcoauth.v1.oauth_pb2.CreateOauthAdminAppRequest,
            grpcoauth.v1.oauth_pb2.CreateOauthAdminAppResponse,
        )
        self.CreateOauthUserApp = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/CreateOauthUserApp',
            grpcoauth.v1.oauth_pb2.CreateOauthUserAppRequest,
            grpcoauth.v1.oauth_pb2.CreateOauthUserAppResponse,
        )
        self.GetAuthorizeCode = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetAuthorizeCode',
            grpcoauth.v1.oauth_pb2.GetAuthorizeCodeRequest,
            grpcoauth.v1.oauth_pb2.GetAuthorizeCodeResponse,
        )
        self.GetToken = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetToken',
            grpcoauth.v1.oauth_pb2.GetTokenRequest,
            grpcoauth.v1.oauth_pb2.GetTokenResponse,
        )
        self.GetAccessTokenInfo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetAccessTokenInfo',
            grpcoauth.v1.oauth_pb2.GetAccessTokenInfoRequest,
            grpcoauth.v1.oauth_pb2.GetAccessTokenInfoResponse,
        )
        self.GetAuthorizeUrl = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthService/GetAuthorizeUrl',
            google.protobuf.empty_pb2.Empty,
            grpcoauth.v1.oauth_pb2.GetAuthorizeUrlResponse,
        )


class OauthCallbackServiceBase(abc.ABC):

    @abc.abstractmethod
    async def NativeCallback(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.NativeCallbackRequest, grpcoauth.v1.oauth_pb2.NativeCallbackResponse]') -> None:
        pass

    @abc.abstractmethod
    async def KakaoCallback(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.KakaoCallbackRequest, grpcoauth.v1.oauth_pb2.KakaoCallbackResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NaverCallback(self, stream: 'grpclib.server.Stream[grpcoauth.v1.oauth_pb2.NaverCallbackRequest, grpcoauth.v1.oauth_pb2.NaverCallbackResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpcoauth.v1.OauthCallbackService/NativeCallback': grpclib.const.Handler(
                self.NativeCallback,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.NativeCallbackRequest,
                grpcoauth.v1.oauth_pb2.NativeCallbackResponse,
            ),
            '/grpcoauth.v1.OauthCallbackService/KakaoCallback': grpclib.const.Handler(
                self.KakaoCallback,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.KakaoCallbackRequest,
                grpcoauth.v1.oauth_pb2.KakaoCallbackResponse,
            ),
            '/grpcoauth.v1.OauthCallbackService/NaverCallback': grpclib.const.Handler(
                self.NaverCallback,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpcoauth.v1.oauth_pb2.NaverCallbackRequest,
                grpcoauth.v1.oauth_pb2.NaverCallbackResponse,
            ),
        }


class OauthCallbackServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.NativeCallback = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthCallbackService/NativeCallback',
            grpcoauth.v1.oauth_pb2.NativeCallbackRequest,
            grpcoauth.v1.oauth_pb2.NativeCallbackResponse,
        )
        self.KakaoCallback = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthCallbackService/KakaoCallback',
            grpcoauth.v1.oauth_pb2.KakaoCallbackRequest,
            grpcoauth.v1.oauth_pb2.KakaoCallbackResponse,
        )
        self.NaverCallback = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpcoauth.v1.OauthCallbackService/NaverCallback',
            grpcoauth.v1.oauth_pb2.NaverCallbackRequest,
            grpcoauth.v1.oauth_pb2.NaverCallbackResponse,
        )
