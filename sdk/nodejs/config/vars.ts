// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

let __config = new pulumi.Config("eventstorecloud");

export let organizationId: string | undefined = __config.get("organizationId");
export let token: string | undefined = __config.get("token");
export let tokenStore: string | undefined = __config.get("tokenStore");
export let url: string | undefined = __config.get("url");
