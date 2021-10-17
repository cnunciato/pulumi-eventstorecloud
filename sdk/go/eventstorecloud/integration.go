// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eventstorecloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages integration resources, for example Slack or OpsGenie.
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
// 		_, err := eventstorecloud.NewIntegration(ctx, "opsgenieIssues", &eventstorecloud.IntegrationArgs{
// 			ProjectId:   pulumi.Any(_var.Project_id),
// 			Description: pulumi.String("create OpsGenie alerts from issues"),
// 			Data: pulumi.AnyMap{
// 				"sink":    pulumi.Any("opsGenie"),
// 				"api_key": pulumi.Any("<secret OpsGenie key here>"),
// 				"source":  pulumi.Any("issues"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = eventstorecloud.NewIntegration(ctx, "slackNotifications", &eventstorecloud.IntegrationArgs{
// 			ProjectId:   pulumi.Any(_var.Project_id),
// 			Description: pulumi.String("send Slack a message when a notification happens"),
// 			Data: pulumi.AnyMap{
// 				"sink":       pulumi.Any("slack"),
// 				"token":      pulumi.Any("<secret token here>"),
// 				"channel_id": pulumi.Any("#esc-cluster-notifications"),
// 				"source":     pulumi.Any("notifications"),
// 			},
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
//  $ pulumi import eventstorecloud:index/integration:Integration opsgenie_issues project_id:integration_id
// ```
type Integration struct {
	pulumi.CustomResourceState

	// Data for the integration
	Data pulumi.MapOutput `pulumi:"data"`
	// Human readable description of the integration
	Description pulumi.StringOutput `pulumi:"description"`
	// ID of the project to which the integration applies
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewIntegration registers a new resource with the given unique name, arguments, and options.
func NewIntegration(ctx *pulumi.Context,
	name string, args *IntegrationArgs, opts ...pulumi.ResourceOption) (*Integration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Data == nil {
		return nil, errors.New("invalid value for required argument 'Data'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	var resource Integration
	err := ctx.RegisterResource("eventstorecloud:index/integration:Integration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIntegration gets an existing Integration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIntegration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IntegrationState, opts ...pulumi.ResourceOption) (*Integration, error) {
	var resource Integration
	err := ctx.ReadResource("eventstorecloud:index/integration:Integration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Integration resources.
type integrationState struct {
	// Data for the integration
	Data map[string]interface{} `pulumi:"data"`
	// Human readable description of the integration
	Description *string `pulumi:"description"`
	// ID of the project to which the integration applies
	ProjectId *string `pulumi:"projectId"`
}

type IntegrationState struct {
	// Data for the integration
	Data pulumi.MapInput
	// Human readable description of the integration
	Description pulumi.StringPtrInput
	// ID of the project to which the integration applies
	ProjectId pulumi.StringPtrInput
}

func (IntegrationState) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationState)(nil)).Elem()
}

type integrationArgs struct {
	// Data for the integration
	Data map[string]interface{} `pulumi:"data"`
	// Human readable description of the integration
	Description string `pulumi:"description"`
	// ID of the project to which the integration applies
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a Integration resource.
type IntegrationArgs struct {
	// Data for the integration
	Data pulumi.MapInput
	// Human readable description of the integration
	Description pulumi.StringInput
	// ID of the project to which the integration applies
	ProjectId pulumi.StringInput
}

func (IntegrationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationArgs)(nil)).Elem()
}

type IntegrationInput interface {
	pulumi.Input

	ToIntegrationOutput() IntegrationOutput
	ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput
}

func (*Integration) ElementType() reflect.Type {
	return reflect.TypeOf((*Integration)(nil))
}

func (i *Integration) ToIntegrationOutput() IntegrationOutput {
	return i.ToIntegrationOutputWithContext(context.Background())
}

func (i *Integration) ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationOutput)
}

func (i *Integration) ToIntegrationPtrOutput() IntegrationPtrOutput {
	return i.ToIntegrationPtrOutputWithContext(context.Background())
}

func (i *Integration) ToIntegrationPtrOutputWithContext(ctx context.Context) IntegrationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationPtrOutput)
}

type IntegrationPtrInput interface {
	pulumi.Input

	ToIntegrationPtrOutput() IntegrationPtrOutput
	ToIntegrationPtrOutputWithContext(ctx context.Context) IntegrationPtrOutput
}

type integrationPtrType IntegrationArgs

func (*integrationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Integration)(nil))
}

func (i *integrationPtrType) ToIntegrationPtrOutput() IntegrationPtrOutput {
	return i.ToIntegrationPtrOutputWithContext(context.Background())
}

func (i *integrationPtrType) ToIntegrationPtrOutputWithContext(ctx context.Context) IntegrationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationPtrOutput)
}

// IntegrationArrayInput is an input type that accepts IntegrationArray and IntegrationArrayOutput values.
// You can construct a concrete instance of `IntegrationArrayInput` via:
//
//          IntegrationArray{ IntegrationArgs{...} }
type IntegrationArrayInput interface {
	pulumi.Input

	ToIntegrationArrayOutput() IntegrationArrayOutput
	ToIntegrationArrayOutputWithContext(context.Context) IntegrationArrayOutput
}

type IntegrationArray []IntegrationInput

func (IntegrationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Integration)(nil)).Elem()
}

func (i IntegrationArray) ToIntegrationArrayOutput() IntegrationArrayOutput {
	return i.ToIntegrationArrayOutputWithContext(context.Background())
}

func (i IntegrationArray) ToIntegrationArrayOutputWithContext(ctx context.Context) IntegrationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationArrayOutput)
}

// IntegrationMapInput is an input type that accepts IntegrationMap and IntegrationMapOutput values.
// You can construct a concrete instance of `IntegrationMapInput` via:
//
//          IntegrationMap{ "key": IntegrationArgs{...} }
type IntegrationMapInput interface {
	pulumi.Input

	ToIntegrationMapOutput() IntegrationMapOutput
	ToIntegrationMapOutputWithContext(context.Context) IntegrationMapOutput
}

type IntegrationMap map[string]IntegrationInput

func (IntegrationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Integration)(nil)).Elem()
}

func (i IntegrationMap) ToIntegrationMapOutput() IntegrationMapOutput {
	return i.ToIntegrationMapOutputWithContext(context.Background())
}

func (i IntegrationMap) ToIntegrationMapOutputWithContext(ctx context.Context) IntegrationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationMapOutput)
}

type IntegrationOutput struct{ *pulumi.OutputState }

func (IntegrationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Integration)(nil))
}

func (o IntegrationOutput) ToIntegrationOutput() IntegrationOutput {
	return o
}

func (o IntegrationOutput) ToIntegrationOutputWithContext(ctx context.Context) IntegrationOutput {
	return o
}

func (o IntegrationOutput) ToIntegrationPtrOutput() IntegrationPtrOutput {
	return o.ToIntegrationPtrOutputWithContext(context.Background())
}

func (o IntegrationOutput) ToIntegrationPtrOutputWithContext(ctx context.Context) IntegrationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Integration) *Integration {
		return &v
	}).(IntegrationPtrOutput)
}

type IntegrationPtrOutput struct{ *pulumi.OutputState }

func (IntegrationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Integration)(nil))
}

func (o IntegrationPtrOutput) ToIntegrationPtrOutput() IntegrationPtrOutput {
	return o
}

func (o IntegrationPtrOutput) ToIntegrationPtrOutputWithContext(ctx context.Context) IntegrationPtrOutput {
	return o
}

func (o IntegrationPtrOutput) Elem() IntegrationOutput {
	return o.ApplyT(func(v *Integration) Integration {
		if v != nil {
			return *v
		}
		var ret Integration
		return ret
	}).(IntegrationOutput)
}

type IntegrationArrayOutput struct{ *pulumi.OutputState }

func (IntegrationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Integration)(nil))
}

func (o IntegrationArrayOutput) ToIntegrationArrayOutput() IntegrationArrayOutput {
	return o
}

func (o IntegrationArrayOutput) ToIntegrationArrayOutputWithContext(ctx context.Context) IntegrationArrayOutput {
	return o
}

func (o IntegrationArrayOutput) Index(i pulumi.IntInput) IntegrationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Integration {
		return vs[0].([]Integration)[vs[1].(int)]
	}).(IntegrationOutput)
}

type IntegrationMapOutput struct{ *pulumi.OutputState }

func (IntegrationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Integration)(nil))
}

func (o IntegrationMapOutput) ToIntegrationMapOutput() IntegrationMapOutput {
	return o
}

func (o IntegrationMapOutput) ToIntegrationMapOutputWithContext(ctx context.Context) IntegrationMapOutput {
	return o
}

func (o IntegrationMapOutput) MapIndex(k pulumi.StringInput) IntegrationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Integration {
		return vs[0].(map[string]Integration)[vs[1].(string)]
	}).(IntegrationOutput)
}

func init() {
	pulumi.RegisterOutputType(IntegrationOutput{})
	pulumi.RegisterOutputType(IntegrationPtrOutput{})
	pulumi.RegisterOutputType(IntegrationArrayOutput{})
	pulumi.RegisterOutputType(IntegrationMapOutput{})
}
