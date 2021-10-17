# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ManagedClusterArgs', 'ManagedCluster']

@pulumi.input_type
class ManagedClusterArgs:
    def __init__(__self__, *,
                 disk_size: pulumi.Input[int],
                 disk_type: pulumi.Input[str],
                 instance_type: pulumi.Input[str],
                 network_id: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 server_version: pulumi.Input[str],
                 topology: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 projection_level: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedCluster resource.
        :param pulumi.Input[int] disk_size: Size of the data disks, in gigabytes
        :param pulumi.Input[str] disk_type: Storage class of the data disks (find the list of valid values below)
        :param pulumi.Input[str] instance_type: Instance type of the managed cluster (find the list of valid values below)
        :param pulumi.Input[str] network_id: ID of the network in which the managed cluster exists
        :param pulumi.Input[str] project_id: ID of the project in which the managed cluster exists
        :param pulumi.Input[str] server_version: Server version to provision (find the list of valid values below)
        :param pulumi.Input[str] topology: Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        :param pulumi.Input[str] name: Name of the managed cluster
        :param pulumi.Input[str] projection_level: Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        """
        pulumi.set(__self__, "disk_size", disk_size)
        pulumi.set(__self__, "disk_type", disk_type)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "server_version", server_version)
        pulumi.set(__self__, "topology", topology)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if projection_level is not None:
            pulumi.set(__self__, "projection_level", projection_level)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Input[int]:
        """
        Size of the data disks, in gigabytes
        """
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> pulumi.Input[str]:
        """
        Storage class of the data disks (find the list of valid values below)
        """
        return pulumi.get(self, "disk_type")

    @disk_type.setter
    def disk_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "disk_type", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        Instance type of the managed cluster (find the list of valid values below)
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        ID of the network in which the managed cluster exists
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        ID of the project in which the managed cluster exists
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> pulumi.Input[str]:
        """
        Server version to provision (find the list of valid values below)
        """
        return pulumi.get(self, "server_version")

    @server_version.setter
    def server_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_version", value)

    @property
    @pulumi.getter
    def topology(self) -> pulumi.Input[str]:
        """
        Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        return pulumi.get(self, "topology")

    @topology.setter
    def topology(self, value: pulumi.Input[str]):
        pulumi.set(self, "topology", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the managed cluster
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectionLevel")
    def projection_level(self) -> Optional[pulumi.Input[str]]:
        """
        Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        """
        return pulumi.get(self, "projection_level")

    @projection_level.setter
    def projection_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "projection_level", value)


@pulumi.input_type
class _ManagedClusterState:
    def __init__(__self__, *,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 disk_type: Optional[pulumi.Input[str]] = None,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 projection_level: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_provider: Optional[pulumi.Input[str]] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 topology: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ManagedCluster resources.
        :param pulumi.Input[int] disk_size: Size of the data disks, in gigabytes
        :param pulumi.Input[str] disk_type: Storage class of the data disks (find the list of valid values below)
        :param pulumi.Input[str] dns_name: DNS address of the cluster
        :param pulumi.Input[str] instance_type: Instance type of the managed cluster (find the list of valid values below)
        :param pulumi.Input[str] name: Name of the managed cluster
        :param pulumi.Input[str] network_id: ID of the network in which the managed cluster exists
        :param pulumi.Input[str] project_id: ID of the project in which the managed cluster exists
        :param pulumi.Input[str] projection_level: Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        :param pulumi.Input[str] region: Region in which the cluster was created. Determined by the region of the Network
        :param pulumi.Input[str] resource_provider: Provider in which the cluster was created. Determined by the provider of the Network.
        :param pulumi.Input[str] server_version: Server version to provision (find the list of valid values below)
        :param pulumi.Input[str] topology: Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        if disk_size is not None:
            pulumi.set(__self__, "disk_size", disk_size)
        if disk_type is not None:
            pulumi.set(__self__, "disk_type", disk_type)
        if dns_name is not None:
            pulumi.set(__self__, "dns_name", dns_name)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if projection_level is not None:
            pulumi.set(__self__, "projection_level", projection_level)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if resource_provider is not None:
            pulumi.set(__self__, "resource_provider", resource_provider)
        if server_version is not None:
            pulumi.set(__self__, "server_version", server_version)
        if topology is not None:
            pulumi.set(__self__, "topology", topology)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[int]]:
        """
        Size of the data disks, in gigabytes
        """
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[str]]:
        """
        Storage class of the data disks (find the list of valid values below)
        """
        return pulumi.get(self, "disk_type")

    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_type", value)

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[str]]:
        """
        DNS address of the cluster
        """
        return pulumi.get(self, "dns_name")

    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_name", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        Instance type of the managed cluster (find the list of valid values below)
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the managed cluster
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the network in which the managed cluster exists
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the project in which the managed cluster exists
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="projectionLevel")
    def projection_level(self) -> Optional[pulumi.Input[str]]:
        """
        Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        """
        return pulumi.get(self, "projection_level")

    @projection_level.setter
    def projection_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "projection_level", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region in which the cluster was created. Determined by the region of the Network
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="resourceProvider")
    def resource_provider(self) -> Optional[pulumi.Input[str]]:
        """
        Provider in which the cluster was created. Determined by the provider of the Network.
        """
        return pulumi.get(self, "resource_provider")

    @resource_provider.setter
    def resource_provider(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_provider", value)

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[str]]:
        """
        Server version to provision (find the list of valid values below)
        """
        return pulumi.get(self, "server_version")

    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_version", value)

    @property
    @pulumi.getter
    def topology(self) -> Optional[pulumi.Input[str]]:
        """
        Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        return pulumi.get(self, "topology")

    @topology.setter
    def topology(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topology", value)


class ManagedCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 disk_type: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 projection_level: Optional[pulumi.Input[str]] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 topology: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages EventStoreDB instances and clusters in Event Store Cloud

        ## Example Usage

        ```python
        import pulumi
        import pulumi_eventstorecloud as eventstorecloud

        example_project = eventstorecloud.get_project(name="Example Project")
        example_network = eventstorecloud.Network("exampleNetwork",
            project_id=eventstorecloud_project["example"]["id"],
            resource_provider="aws",
            region="us-west-2",
            cidr_block="172.21.0.0/16")
        example_managed_cluster = eventstorecloud.ManagedCluster("exampleManagedCluster",
            project_id=example_network.project_id,
            network_id=example_network.id,
            topology="three-node-multi-zone",
            instance_type="F1",
            disk_size=24,
            disk_type="gp2",
            server_version="20.6")
        ```

        ## Import

        ```sh
         $ pulumi import eventstorecloud:index/managedCluster:ManagedCluster example project_id:cluster_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] disk_size: Size of the data disks, in gigabytes
        :param pulumi.Input[str] disk_type: Storage class of the data disks (find the list of valid values below)
        :param pulumi.Input[str] instance_type: Instance type of the managed cluster (find the list of valid values below)
        :param pulumi.Input[str] name: Name of the managed cluster
        :param pulumi.Input[str] network_id: ID of the network in which the managed cluster exists
        :param pulumi.Input[str] project_id: ID of the project in which the managed cluster exists
        :param pulumi.Input[str] projection_level: Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        :param pulumi.Input[str] server_version: Server version to provision (find the list of valid values below)
        :param pulumi.Input[str] topology: Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages EventStoreDB instances and clusters in Event Store Cloud

        ## Example Usage

        ```python
        import pulumi
        import pulumi_eventstorecloud as eventstorecloud

        example_project = eventstorecloud.get_project(name="Example Project")
        example_network = eventstorecloud.Network("exampleNetwork",
            project_id=eventstorecloud_project["example"]["id"],
            resource_provider="aws",
            region="us-west-2",
            cidr_block="172.21.0.0/16")
        example_managed_cluster = eventstorecloud.ManagedCluster("exampleManagedCluster",
            project_id=example_network.project_id,
            network_id=example_network.id,
            topology="three-node-multi-zone",
            instance_type="F1",
            disk_size=24,
            disk_type="gp2",
            server_version="20.6")
        ```

        ## Import

        ```sh
         $ pulumi import eventstorecloud:index/managedCluster:ManagedCluster example project_id:cluster_id
        ```

        :param str resource_name: The name of the resource.
        :param ManagedClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 disk_type: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 projection_level: Optional[pulumi.Input[str]] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 topology: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedClusterArgs.__new__(ManagedClusterArgs)

            if disk_size is None and not opts.urn:
                raise TypeError("Missing required property 'disk_size'")
            __props__.__dict__["disk_size"] = disk_size
            if disk_type is None and not opts.urn:
                raise TypeError("Missing required property 'disk_type'")
            __props__.__dict__["disk_type"] = disk_type
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["projection_level"] = projection_level
            if server_version is None and not opts.urn:
                raise TypeError("Missing required property 'server_version'")
            __props__.__dict__["server_version"] = server_version
            if topology is None and not opts.urn:
                raise TypeError("Missing required property 'topology'")
            __props__.__dict__["topology"] = topology
            __props__.__dict__["dns_name"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["resource_provider"] = None
        super(ManagedCluster, __self__).__init__(
            'eventstorecloud:index/managedCluster:ManagedCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            disk_size: Optional[pulumi.Input[int]] = None,
            disk_type: Optional[pulumi.Input[str]] = None,
            dns_name: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            projection_level: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            resource_provider: Optional[pulumi.Input[str]] = None,
            server_version: Optional[pulumi.Input[str]] = None,
            topology: Optional[pulumi.Input[str]] = None) -> 'ManagedCluster':
        """
        Get an existing ManagedCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] disk_size: Size of the data disks, in gigabytes
        :param pulumi.Input[str] disk_type: Storage class of the data disks (find the list of valid values below)
        :param pulumi.Input[str] dns_name: DNS address of the cluster
        :param pulumi.Input[str] instance_type: Instance type of the managed cluster (find the list of valid values below)
        :param pulumi.Input[str] name: Name of the managed cluster
        :param pulumi.Input[str] network_id: ID of the network in which the managed cluster exists
        :param pulumi.Input[str] project_id: ID of the project in which the managed cluster exists
        :param pulumi.Input[str] projection_level: Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        :param pulumi.Input[str] region: Region in which the cluster was created. Determined by the region of the Network
        :param pulumi.Input[str] resource_provider: Provider in which the cluster was created. Determined by the provider of the Network.
        :param pulumi.Input[str] server_version: Server version to provision (find the list of valid values below)
        :param pulumi.Input[str] topology: Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedClusterState.__new__(_ManagedClusterState)

        __props__.__dict__["disk_size"] = disk_size
        __props__.__dict__["disk_type"] = disk_type
        __props__.__dict__["dns_name"] = dns_name
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["projection_level"] = projection_level
        __props__.__dict__["region"] = region
        __props__.__dict__["resource_provider"] = resource_provider
        __props__.__dict__["server_version"] = server_version
        __props__.__dict__["topology"] = topology
        return ManagedCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Output[int]:
        """
        Size of the data disks, in gigabytes
        """
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> pulumi.Output[str]:
        """
        Storage class of the data disks (find the list of valid values below)
        """
        return pulumi.get(self, "disk_type")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[str]:
        """
        DNS address of the cluster
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        Instance type of the managed cluster (find the list of valid values below)
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the managed cluster
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        ID of the network in which the managed cluster exists
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        ID of the project in which the managed cluster exists
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectionLevel")
    def projection_level(self) -> pulumi.Output[Optional[str]]:
        """
        Determines whether to run no projections, system projections only, or system and user projections (find the list of valid values below) Defaults to `off`.
        """
        return pulumi.get(self, "projection_level")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region in which the cluster was created. Determined by the region of the Network
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceProvider")
    def resource_provider(self) -> pulumi.Output[str]:
        """
        Provider in which the cluster was created. Determined by the provider of the Network.
        """
        return pulumi.get(self, "resource_provider")

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> pulumi.Output[str]:
        """
        Server version to provision (find the list of valid values below)
        """
        return pulumi.get(self, "server_version")

    @property
    @pulumi.getter
    def topology(self) -> pulumi.Output[str]:
        """
        Topology of the managed cluster (`single-node` or `three-node-multi-zone`)
        """
        return pulumi.get(self, "topology")

