// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventstorecloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages VPC (network) resources in Event Store Cloud
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-eventstorecloud/sdk/go/eventstorecloud"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleProject, err := eventstorecloud.NewProject(ctx, "exampleProject", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = eventstorecloud.NewNetwork(ctx, "exampleNetwork", &eventstorecloud.NetworkArgs{
// 			ProjectId:        exampleProject.ID(),
// 			ResourceProvider: pulumi.String("aws"),
// 			Region:           pulumi.String("us-west-2"),
// 			CidrBlock:        pulumi.String("172.21.0.0/16"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// ```sh
//  $ pulumi import eventstorecloud:index/network:Network example project_id:network_id
// ```
type Network struct {
	pulumi.CustomResourceState

	// Address space of the network in CIDR block notation
	CidrBlock pulumi.StringOutput `pulumi:"cidrBlock"`
	// Human-friendly name for the network
	Name pulumi.StringOutput `pulumi:"name"`
	// Project ID
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Provider region in which to provision the network
	Region pulumi.StringOutput `pulumi:"region"`
	// Cloud Provider in which to provision the network.
	ResourceProvider pulumi.StringOutput `pulumi:"resourceProvider"`
}

// NewNetwork registers a new resource with the given unique name, arguments, and options.
func NewNetwork(ctx *pulumi.Context,
	name string, args *NetworkArgs, opts ...pulumi.ResourceOption) (*Network, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CidrBlock == nil {
		return nil, errors.New("invalid value for required argument 'CidrBlock'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	if args.Region == nil {
		return nil, errors.New("invalid value for required argument 'Region'")
	}
	if args.ResourceProvider == nil {
		return nil, errors.New("invalid value for required argument 'ResourceProvider'")
	}
	var resource Network
	err := ctx.RegisterResource("eventstorecloud:index/network:Network", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetwork gets an existing Network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkState, opts ...pulumi.ResourceOption) (*Network, error) {
	var resource Network
	err := ctx.ReadResource("eventstorecloud:index/network:Network", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Network resources.
type networkState struct {
	// Address space of the network in CIDR block notation
	CidrBlock *string `pulumi:"cidrBlock"`
	// Human-friendly name for the network
	Name *string `pulumi:"name"`
	// Project ID
	ProjectId *string `pulumi:"projectId"`
	// Provider region in which to provision the network
	Region *string `pulumi:"region"`
	// Cloud Provider in which to provision the network.
	ResourceProvider *string `pulumi:"resourceProvider"`
}

type NetworkState struct {
	// Address space of the network in CIDR block notation
	CidrBlock pulumi.StringPtrInput
	// Human-friendly name for the network
	Name pulumi.StringPtrInput
	// Project ID
	ProjectId pulumi.StringPtrInput
	// Provider region in which to provision the network
	Region pulumi.StringPtrInput
	// Cloud Provider in which to provision the network.
	ResourceProvider pulumi.StringPtrInput
}

func (NetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkState)(nil)).Elem()
}

type networkArgs struct {
	// Address space of the network in CIDR block notation
	CidrBlock string `pulumi:"cidrBlock"`
	// Human-friendly name for the network
	Name *string `pulumi:"name"`
	// Project ID
	ProjectId string `pulumi:"projectId"`
	// Provider region in which to provision the network
	Region string `pulumi:"region"`
	// Cloud Provider in which to provision the network.
	ResourceProvider string `pulumi:"resourceProvider"`
}

// The set of arguments for constructing a Network resource.
type NetworkArgs struct {
	// Address space of the network in CIDR block notation
	CidrBlock pulumi.StringInput
	// Human-friendly name for the network
	Name pulumi.StringPtrInput
	// Project ID
	ProjectId pulumi.StringInput
	// Provider region in which to provision the network
	Region pulumi.StringInput
	// Cloud Provider in which to provision the network.
	ResourceProvider pulumi.StringInput
}

func (NetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkArgs)(nil)).Elem()
}

type NetworkInput interface {
	pulumi.Input

	ToNetworkOutput() NetworkOutput
	ToNetworkOutputWithContext(ctx context.Context) NetworkOutput
}

func (*Network) ElementType() reflect.Type {
	return reflect.TypeOf((*Network)(nil))
}

func (i *Network) ToNetworkOutput() NetworkOutput {
	return i.ToNetworkOutputWithContext(context.Background())
}

func (i *Network) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkOutput)
}

func (i *Network) ToNetworkPtrOutput() NetworkPtrOutput {
	return i.ToNetworkPtrOutputWithContext(context.Background())
}

func (i *Network) ToNetworkPtrOutputWithContext(ctx context.Context) NetworkPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkPtrOutput)
}

type NetworkPtrInput interface {
	pulumi.Input

	ToNetworkPtrOutput() NetworkPtrOutput
	ToNetworkPtrOutputWithContext(ctx context.Context) NetworkPtrOutput
}

type networkPtrType NetworkArgs

func (*networkPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil))
}

func (i *networkPtrType) ToNetworkPtrOutput() NetworkPtrOutput {
	return i.ToNetworkPtrOutputWithContext(context.Background())
}

func (i *networkPtrType) ToNetworkPtrOutputWithContext(ctx context.Context) NetworkPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkPtrOutput)
}

// NetworkArrayInput is an input type that accepts NetworkArray and NetworkArrayOutput values.
// You can construct a concrete instance of `NetworkArrayInput` via:
//
//          NetworkArray{ NetworkArgs{...} }
type NetworkArrayInput interface {
	pulumi.Input

	ToNetworkArrayOutput() NetworkArrayOutput
	ToNetworkArrayOutputWithContext(context.Context) NetworkArrayOutput
}

type NetworkArray []NetworkInput

func (NetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Network)(nil)).Elem()
}

func (i NetworkArray) ToNetworkArrayOutput() NetworkArrayOutput {
	return i.ToNetworkArrayOutputWithContext(context.Background())
}

func (i NetworkArray) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkArrayOutput)
}

// NetworkMapInput is an input type that accepts NetworkMap and NetworkMapOutput values.
// You can construct a concrete instance of `NetworkMapInput` via:
//
//          NetworkMap{ "key": NetworkArgs{...} }
type NetworkMapInput interface {
	pulumi.Input

	ToNetworkMapOutput() NetworkMapOutput
	ToNetworkMapOutputWithContext(context.Context) NetworkMapOutput
}

type NetworkMap map[string]NetworkInput

func (NetworkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Network)(nil)).Elem()
}

func (i NetworkMap) ToNetworkMapOutput() NetworkMapOutput {
	return i.ToNetworkMapOutputWithContext(context.Background())
}

func (i NetworkMap) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkMapOutput)
}

type NetworkOutput struct{ *pulumi.OutputState }

func (NetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Network)(nil))
}

func (o NetworkOutput) ToNetworkOutput() NetworkOutput {
	return o
}

func (o NetworkOutput) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return o
}

func (o NetworkOutput) ToNetworkPtrOutput() NetworkPtrOutput {
	return o.ToNetworkPtrOutputWithContext(context.Background())
}

func (o NetworkOutput) ToNetworkPtrOutputWithContext(ctx context.Context) NetworkPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Network) *Network {
		return &v
	}).(NetworkPtrOutput)
}

type NetworkPtrOutput struct{ *pulumi.OutputState }

func (NetworkPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil))
}

func (o NetworkPtrOutput) ToNetworkPtrOutput() NetworkPtrOutput {
	return o
}

func (o NetworkPtrOutput) ToNetworkPtrOutputWithContext(ctx context.Context) NetworkPtrOutput {
	return o
}

func (o NetworkPtrOutput) Elem() NetworkOutput {
	return o.ApplyT(func(v *Network) Network {
		if v != nil {
			return *v
		}
		var ret Network
		return ret
	}).(NetworkOutput)
}

type NetworkArrayOutput struct{ *pulumi.OutputState }

func (NetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Network)(nil))
}

func (o NetworkArrayOutput) ToNetworkArrayOutput() NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) Index(i pulumi.IntInput) NetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Network {
		return vs[0].([]Network)[vs[1].(int)]
	}).(NetworkOutput)
}

type NetworkMapOutput struct{ *pulumi.OutputState }

func (NetworkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Network)(nil))
}

func (o NetworkMapOutput) ToNetworkMapOutput() NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) MapIndex(k pulumi.StringInput) NetworkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Network {
		return vs[0].(map[string]Network)[vs[1].(string)]
	}).(NetworkOutput)
}

func init() {
	pulumi.RegisterOutputType(NetworkOutput{})
	pulumi.RegisterOutputType(NetworkPtrOutput{})
	pulumi.RegisterOutputType(NetworkArrayOutput{})
	pulumi.RegisterOutputType(NetworkMapOutput{})
}
