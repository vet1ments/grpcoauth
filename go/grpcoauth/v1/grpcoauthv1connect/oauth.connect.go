// Code generated by protoc-gen-connect-go. DO NOT EDIT.
//
// Source: grpcoauth/v1/oauth.proto

package grpcoauthv1connect

import (
	connect "connectrpc.com/connect"
	context "context"
	errors "errors"
	v1 "github.com/vet1ments/grpcoauth/go/grpcoauth/v1"
	http "net/http"
	strings "strings"
)

// This is a compile-time assertion to ensure that this generated file and the connect package are
// compatible. If you get a compiler error that this constant is not defined, this code was
// generated with a version of connect newer than the one compiled into your binary. You can fix the
// problem by either regenerating this code with an older version of connect or updating the connect
// version compiled into your binary.
const _ = connect.IsAtLeastVersion1_13_0

const (
	// OauthServiceName is the fully-qualified name of the OauthService service.
	OauthServiceName = "grpcoauth.v1.OauthService"
)

// These constants are the fully-qualified names of the RPCs defined in this package. They're
// exposed at runtime as Spec.Procedure and as the final two segments of the HTTP route.
//
// Note that these are different from the fully-qualified method names used by
// google.golang.org/protobuf/reflect/protoreflect. To convert from these constants to
// reflection-formatted method names, remove the leading slash and convert the remaining slash to a
// period.
const (
	// OauthServiceGetOauthAppTokenInfoProcedure is the fully-qualified name of the OauthService's
	// GetOauthAppTokenInfo RPC.
	OauthServiceGetOauthAppTokenInfoProcedure = "/grpcoauth.v1.OauthService/GetOauthAppTokenInfo"
	// OauthServiceGetOauthAppUserProcedure is the fully-qualified name of the OauthService's
	// GetOauthAppUser RPC.
	OauthServiceGetOauthAppUserProcedure = "/grpcoauth.v1.OauthService/GetOauthAppUser"
	// OauthServiceGetOauthAppUserListProcedure is the fully-qualified name of the OauthService's
	// GetOauthAppUserList RPC.
	OauthServiceGetOauthAppUserListProcedure = "/grpcoauth.v1.OauthService/GetOauthAppUserList"
	// OauthServiceCreateOauthAdminAppProcedure is the fully-qualified name of the OauthService's
	// CreateOauthAdminApp RPC.
	OauthServiceCreateOauthAdminAppProcedure = "/grpcoauth.v1.OauthService/CreateOauthAdminApp"
	// OauthServiceCreateOauthUserAppProcedure is the fully-qualified name of the OauthService's
	// CreateOauthUserApp RPC.
	OauthServiceCreateOauthUserAppProcedure = "/grpcoauth.v1.OauthService/CreateOauthUserApp"
	// OauthServiceGetAuthorizeCodeProcedure is the fully-qualified name of the OauthService's
	// GetAuthorizeCode RPC.
	OauthServiceGetAuthorizeCodeProcedure = "/grpcoauth.v1.OauthService/GetAuthorizeCode"
	// OauthServiceGetTokenProcedure is the fully-qualified name of the OauthService's GetToken RPC.
	OauthServiceGetTokenProcedure = "/grpcoauth.v1.OauthService/GetToken"
)

// These variables are the protoreflect.Descriptor objects for the RPCs defined in this package.
var (
	oauthServiceServiceDescriptor                    = v1.File_grpcoauth_v1_oauth_proto.Services().ByName("OauthService")
	oauthServiceGetOauthAppTokenInfoMethodDescriptor = oauthServiceServiceDescriptor.Methods().ByName("GetOauthAppTokenInfo")
	oauthServiceGetOauthAppUserMethodDescriptor      = oauthServiceServiceDescriptor.Methods().ByName("GetOauthAppUser")
	oauthServiceGetOauthAppUserListMethodDescriptor  = oauthServiceServiceDescriptor.Methods().ByName("GetOauthAppUserList")
	oauthServiceCreateOauthAdminAppMethodDescriptor  = oauthServiceServiceDescriptor.Methods().ByName("CreateOauthAdminApp")
	oauthServiceCreateOauthUserAppMethodDescriptor   = oauthServiceServiceDescriptor.Methods().ByName("CreateOauthUserApp")
	oauthServiceGetAuthorizeCodeMethodDescriptor     = oauthServiceServiceDescriptor.Methods().ByName("GetAuthorizeCode")
	oauthServiceGetTokenMethodDescriptor             = oauthServiceServiceDescriptor.Methods().ByName("GetToken")
)

// OauthServiceClient is a client for the grpcoauth.v1.OauthService service.
type OauthServiceClient interface {
	GetOauthAppTokenInfo(context.Context, *connect.Request[v1.GetOauthAppTokenInfoRequest]) (*connect.Response[v1.GetOauthAppTokenInfoResponse], error)
	GetOauthAppUser(context.Context, *connect.Request[v1.GetOauthAppUserRequest]) (*connect.Response[v1.GetOauthAppUserResponse], error)
	GetOauthAppUserList(context.Context, *connect.Request[v1.GetOauthAppUserListRequest]) (*connect.Response[v1.GetOauthAppUserListResponse], error)
	CreateOauthAdminApp(context.Context, *connect.Request[v1.CreateOauthAdminAppRequest]) (*connect.Response[v1.CreateOauthAdminAppResponse], error)
	CreateOauthUserApp(context.Context, *connect.Request[v1.CreateOauthUserAppRequest]) (*connect.Response[v1.CreateOauthUserAppResponse], error)
	GetAuthorizeCode(context.Context, *connect.Request[v1.GetAuthorizeCodeRequest]) (*connect.Response[v1.GetAuthorizeCodeResponse], error)
	GetToken(context.Context, *connect.Request[v1.GetTokenRequest]) (*connect.Response[v1.GetTokenResponse], error)
}

// NewOauthServiceClient constructs a client for the grpcoauth.v1.OauthService service. By default,
// it uses the Connect protocol with the binary Protobuf Codec, asks for gzipped responses, and
// sends uncompressed requests. To use the gRPC or gRPC-Web protocols, supply the connect.WithGRPC()
// or connect.WithGRPCWeb() options.
//
// The URL supplied here should be the base URL for the Connect or gRPC server (for example,
// http://api.acme.com or https://acme.com/grpc).
func NewOauthServiceClient(httpClient connect.HTTPClient, baseURL string, opts ...connect.ClientOption) OauthServiceClient {
	baseURL = strings.TrimRight(baseURL, "/")
	return &oauthServiceClient{
		getOauthAppTokenInfo: connect.NewClient[v1.GetOauthAppTokenInfoRequest, v1.GetOauthAppTokenInfoResponse](
			httpClient,
			baseURL+OauthServiceGetOauthAppTokenInfoProcedure,
			connect.WithSchema(oauthServiceGetOauthAppTokenInfoMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getOauthAppUser: connect.NewClient[v1.GetOauthAppUserRequest, v1.GetOauthAppUserResponse](
			httpClient,
			baseURL+OauthServiceGetOauthAppUserProcedure,
			connect.WithSchema(oauthServiceGetOauthAppUserMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getOauthAppUserList: connect.NewClient[v1.GetOauthAppUserListRequest, v1.GetOauthAppUserListResponse](
			httpClient,
			baseURL+OauthServiceGetOauthAppUserListProcedure,
			connect.WithSchema(oauthServiceGetOauthAppUserListMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		createOauthAdminApp: connect.NewClient[v1.CreateOauthAdminAppRequest, v1.CreateOauthAdminAppResponse](
			httpClient,
			baseURL+OauthServiceCreateOauthAdminAppProcedure,
			connect.WithSchema(oauthServiceCreateOauthAdminAppMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		createOauthUserApp: connect.NewClient[v1.CreateOauthUserAppRequest, v1.CreateOauthUserAppResponse](
			httpClient,
			baseURL+OauthServiceCreateOauthUserAppProcedure,
			connect.WithSchema(oauthServiceCreateOauthUserAppMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getAuthorizeCode: connect.NewClient[v1.GetAuthorizeCodeRequest, v1.GetAuthorizeCodeResponse](
			httpClient,
			baseURL+OauthServiceGetAuthorizeCodeProcedure,
			connect.WithSchema(oauthServiceGetAuthorizeCodeMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		getToken: connect.NewClient[v1.GetTokenRequest, v1.GetTokenResponse](
			httpClient,
			baseURL+OauthServiceGetTokenProcedure,
			connect.WithSchema(oauthServiceGetTokenMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
	}
}

// oauthServiceClient implements OauthServiceClient.
type oauthServiceClient struct {
	getOauthAppTokenInfo *connect.Client[v1.GetOauthAppTokenInfoRequest, v1.GetOauthAppTokenInfoResponse]
	getOauthAppUser      *connect.Client[v1.GetOauthAppUserRequest, v1.GetOauthAppUserResponse]
	getOauthAppUserList  *connect.Client[v1.GetOauthAppUserListRequest, v1.GetOauthAppUserListResponse]
	createOauthAdminApp  *connect.Client[v1.CreateOauthAdminAppRequest, v1.CreateOauthAdminAppResponse]
	createOauthUserApp   *connect.Client[v1.CreateOauthUserAppRequest, v1.CreateOauthUserAppResponse]
	getAuthorizeCode     *connect.Client[v1.GetAuthorizeCodeRequest, v1.GetAuthorizeCodeResponse]
	getToken             *connect.Client[v1.GetTokenRequest, v1.GetTokenResponse]
}

// GetOauthAppTokenInfo calls grpcoauth.v1.OauthService.GetOauthAppTokenInfo.
func (c *oauthServiceClient) GetOauthAppTokenInfo(ctx context.Context, req *connect.Request[v1.GetOauthAppTokenInfoRequest]) (*connect.Response[v1.GetOauthAppTokenInfoResponse], error) {
	return c.getOauthAppTokenInfo.CallUnary(ctx, req)
}

// GetOauthAppUser calls grpcoauth.v1.OauthService.GetOauthAppUser.
func (c *oauthServiceClient) GetOauthAppUser(ctx context.Context, req *connect.Request[v1.GetOauthAppUserRequest]) (*connect.Response[v1.GetOauthAppUserResponse], error) {
	return c.getOauthAppUser.CallUnary(ctx, req)
}

// GetOauthAppUserList calls grpcoauth.v1.OauthService.GetOauthAppUserList.
func (c *oauthServiceClient) GetOauthAppUserList(ctx context.Context, req *connect.Request[v1.GetOauthAppUserListRequest]) (*connect.Response[v1.GetOauthAppUserListResponse], error) {
	return c.getOauthAppUserList.CallUnary(ctx, req)
}

// CreateOauthAdminApp calls grpcoauth.v1.OauthService.CreateOauthAdminApp.
func (c *oauthServiceClient) CreateOauthAdminApp(ctx context.Context, req *connect.Request[v1.CreateOauthAdminAppRequest]) (*connect.Response[v1.CreateOauthAdminAppResponse], error) {
	return c.createOauthAdminApp.CallUnary(ctx, req)
}

// CreateOauthUserApp calls grpcoauth.v1.OauthService.CreateOauthUserApp.
func (c *oauthServiceClient) CreateOauthUserApp(ctx context.Context, req *connect.Request[v1.CreateOauthUserAppRequest]) (*connect.Response[v1.CreateOauthUserAppResponse], error) {
	return c.createOauthUserApp.CallUnary(ctx, req)
}

// GetAuthorizeCode calls grpcoauth.v1.OauthService.GetAuthorizeCode.
func (c *oauthServiceClient) GetAuthorizeCode(ctx context.Context, req *connect.Request[v1.GetAuthorizeCodeRequest]) (*connect.Response[v1.GetAuthorizeCodeResponse], error) {
	return c.getAuthorizeCode.CallUnary(ctx, req)
}

// GetToken calls grpcoauth.v1.OauthService.GetToken.
func (c *oauthServiceClient) GetToken(ctx context.Context, req *connect.Request[v1.GetTokenRequest]) (*connect.Response[v1.GetTokenResponse], error) {
	return c.getToken.CallUnary(ctx, req)
}

// OauthServiceHandler is an implementation of the grpcoauth.v1.OauthService service.
type OauthServiceHandler interface {
	GetOauthAppTokenInfo(context.Context, *connect.Request[v1.GetOauthAppTokenInfoRequest]) (*connect.Response[v1.GetOauthAppTokenInfoResponse], error)
	GetOauthAppUser(context.Context, *connect.Request[v1.GetOauthAppUserRequest]) (*connect.Response[v1.GetOauthAppUserResponse], error)
	GetOauthAppUserList(context.Context, *connect.Request[v1.GetOauthAppUserListRequest]) (*connect.Response[v1.GetOauthAppUserListResponse], error)
	CreateOauthAdminApp(context.Context, *connect.Request[v1.CreateOauthAdminAppRequest]) (*connect.Response[v1.CreateOauthAdminAppResponse], error)
	CreateOauthUserApp(context.Context, *connect.Request[v1.CreateOauthUserAppRequest]) (*connect.Response[v1.CreateOauthUserAppResponse], error)
	GetAuthorizeCode(context.Context, *connect.Request[v1.GetAuthorizeCodeRequest]) (*connect.Response[v1.GetAuthorizeCodeResponse], error)
	GetToken(context.Context, *connect.Request[v1.GetTokenRequest]) (*connect.Response[v1.GetTokenResponse], error)
}

// NewOauthServiceHandler builds an HTTP handler from the service implementation. It returns the
// path on which to mount the handler and the handler itself.
//
// By default, handlers support the Connect, gRPC, and gRPC-Web protocols with the binary Protobuf
// and JSON codecs. They also support gzip compression.
func NewOauthServiceHandler(svc OauthServiceHandler, opts ...connect.HandlerOption) (string, http.Handler) {
	oauthServiceGetOauthAppTokenInfoHandler := connect.NewUnaryHandler(
		OauthServiceGetOauthAppTokenInfoProcedure,
		svc.GetOauthAppTokenInfo,
		connect.WithSchema(oauthServiceGetOauthAppTokenInfoMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceGetOauthAppUserHandler := connect.NewUnaryHandler(
		OauthServiceGetOauthAppUserProcedure,
		svc.GetOauthAppUser,
		connect.WithSchema(oauthServiceGetOauthAppUserMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceGetOauthAppUserListHandler := connect.NewUnaryHandler(
		OauthServiceGetOauthAppUserListProcedure,
		svc.GetOauthAppUserList,
		connect.WithSchema(oauthServiceGetOauthAppUserListMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceCreateOauthAdminAppHandler := connect.NewUnaryHandler(
		OauthServiceCreateOauthAdminAppProcedure,
		svc.CreateOauthAdminApp,
		connect.WithSchema(oauthServiceCreateOauthAdminAppMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceCreateOauthUserAppHandler := connect.NewUnaryHandler(
		OauthServiceCreateOauthUserAppProcedure,
		svc.CreateOauthUserApp,
		connect.WithSchema(oauthServiceCreateOauthUserAppMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceGetAuthorizeCodeHandler := connect.NewUnaryHandler(
		OauthServiceGetAuthorizeCodeProcedure,
		svc.GetAuthorizeCode,
		connect.WithSchema(oauthServiceGetAuthorizeCodeMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	oauthServiceGetTokenHandler := connect.NewUnaryHandler(
		OauthServiceGetTokenProcedure,
		svc.GetToken,
		connect.WithSchema(oauthServiceGetTokenMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	return "/grpcoauth.v1.OauthService/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case OauthServiceGetOauthAppTokenInfoProcedure:
			oauthServiceGetOauthAppTokenInfoHandler.ServeHTTP(w, r)
		case OauthServiceGetOauthAppUserProcedure:
			oauthServiceGetOauthAppUserHandler.ServeHTTP(w, r)
		case OauthServiceGetOauthAppUserListProcedure:
			oauthServiceGetOauthAppUserListHandler.ServeHTTP(w, r)
		case OauthServiceCreateOauthAdminAppProcedure:
			oauthServiceCreateOauthAdminAppHandler.ServeHTTP(w, r)
		case OauthServiceCreateOauthUserAppProcedure:
			oauthServiceCreateOauthUserAppHandler.ServeHTTP(w, r)
		case OauthServiceGetAuthorizeCodeProcedure:
			oauthServiceGetAuthorizeCodeHandler.ServeHTTP(w, r)
		case OauthServiceGetTokenProcedure:
			oauthServiceGetTokenHandler.ServeHTTP(w, r)
		default:
			http.NotFound(w, r)
		}
	})
}

// UnimplementedOauthServiceHandler returns CodeUnimplemented from all methods.
type UnimplementedOauthServiceHandler struct{}

func (UnimplementedOauthServiceHandler) GetOauthAppTokenInfo(context.Context, *connect.Request[v1.GetOauthAppTokenInfoRequest]) (*connect.Response[v1.GetOauthAppTokenInfoResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.GetOauthAppTokenInfo is not implemented"))
}

func (UnimplementedOauthServiceHandler) GetOauthAppUser(context.Context, *connect.Request[v1.GetOauthAppUserRequest]) (*connect.Response[v1.GetOauthAppUserResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.GetOauthAppUser is not implemented"))
}

func (UnimplementedOauthServiceHandler) GetOauthAppUserList(context.Context, *connect.Request[v1.GetOauthAppUserListRequest]) (*connect.Response[v1.GetOauthAppUserListResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.GetOauthAppUserList is not implemented"))
}

func (UnimplementedOauthServiceHandler) CreateOauthAdminApp(context.Context, *connect.Request[v1.CreateOauthAdminAppRequest]) (*connect.Response[v1.CreateOauthAdminAppResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.CreateOauthAdminApp is not implemented"))
}

func (UnimplementedOauthServiceHandler) CreateOauthUserApp(context.Context, *connect.Request[v1.CreateOauthUserAppRequest]) (*connect.Response[v1.CreateOauthUserAppResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.CreateOauthUserApp is not implemented"))
}

func (UnimplementedOauthServiceHandler) GetAuthorizeCode(context.Context, *connect.Request[v1.GetAuthorizeCodeRequest]) (*connect.Response[v1.GetAuthorizeCodeResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.GetAuthorizeCode is not implemented"))
}

func (UnimplementedOauthServiceHandler) GetToken(context.Context, *connect.Request[v1.GetTokenRequest]) (*connect.Response[v1.GetTokenResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("grpcoauth.v1.OauthService.GetToken is not implemented"))
}
