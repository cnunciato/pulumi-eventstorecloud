# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ScheduledBackupArgs', 'ScheduledBackup']

@pulumi.input_type
class ScheduledBackupArgs:
    def __init__(__self__, *,
                 backup_description: pulumi.Input[str],
                 description: pulumi.Input[str],
                 max_backup_count: pulumi.Input[int],
                 project_id: pulumi.Input[str],
                 schedule: pulumi.Input[str],
                 source_cluster_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ScheduledBackup resource.
        :param pulumi.Input[str] backup_description: backup_description
        :param pulumi.Input[str] description: Human readable description of the job
        :param pulumi.Input[int] max_backup_count: The maximum number of backups to keep for this job
        :param pulumi.Input[str] project_id: ID of the project in which the backup exists
        :param pulumi.Input[str] schedule: Schedule for the backup, defined using restricted subset of cron
        :param pulumi.Input[str] source_cluster_id: the ID of the cluster to back up
        """
        pulumi.set(__self__, "backup_description", backup_description)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "max_backup_count", max_backup_count)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "schedule", schedule)
        pulumi.set(__self__, "source_cluster_id", source_cluster_id)

    @property
    @pulumi.getter(name="backupDescription")
    def backup_description(self) -> pulumi.Input[str]:
        """
        backup_description
        """
        return pulumi.get(self, "backup_description")

    @backup_description.setter
    def backup_description(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_description", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Human readable description of the job
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxBackupCount")
    def max_backup_count(self) -> pulumi.Input[int]:
        """
        The maximum number of backups to keep for this job
        """
        return pulumi.get(self, "max_backup_count")

    @max_backup_count.setter
    def max_backup_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_backup_count", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        ID of the project in which the backup exists
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[str]:
        """
        Schedule for the backup, defined using restricted subset of cron
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input[str]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="sourceClusterId")
    def source_cluster_id(self) -> pulumi.Input[str]:
        """
        the ID of the cluster to back up
        """
        return pulumi.get(self, "source_cluster_id")

    @source_cluster_id.setter
    def source_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_cluster_id", value)


@pulumi.input_type
class _ScheduledBackupState:
    def __init__(__self__, *,
                 backup_description: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_backup_count: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 source_cluster_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ScheduledBackup resources.
        :param pulumi.Input[str] backup_description: backup_description
        :param pulumi.Input[str] description: Human readable description of the job
        :param pulumi.Input[int] max_backup_count: The maximum number of backups to keep for this job
        :param pulumi.Input[str] project_id: ID of the project in which the backup exists
        :param pulumi.Input[str] schedule: Schedule for the backup, defined using restricted subset of cron
        :param pulumi.Input[str] source_cluster_id: the ID of the cluster to back up
        """
        if backup_description is not None:
            pulumi.set(__self__, "backup_description", backup_description)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if max_backup_count is not None:
            pulumi.set(__self__, "max_backup_count", max_backup_count)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if source_cluster_id is not None:
            pulumi.set(__self__, "source_cluster_id", source_cluster_id)

    @property
    @pulumi.getter(name="backupDescription")
    def backup_description(self) -> Optional[pulumi.Input[str]]:
        """
        backup_description
        """
        return pulumi.get(self, "backup_description")

    @backup_description.setter
    def backup_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_description", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable description of the job
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxBackupCount")
    def max_backup_count(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of backups to keep for this job
        """
        return pulumi.get(self, "max_backup_count")

    @max_backup_count.setter
    def max_backup_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_backup_count", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the project in which the backup exists
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Schedule for the backup, defined using restricted subset of cron
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="sourceClusterId")
    def source_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        the ID of the cluster to back up
        """
        return pulumi.get(self, "source_cluster_id")

    @source_cluster_id.setter
    def source_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_cluster_id", value)


class ScheduledBackup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_description: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_backup_count: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 source_cluster_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ScheduledBackup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_description: backup_description
        :param pulumi.Input[str] description: Human readable description of the job
        :param pulumi.Input[int] max_backup_count: The maximum number of backups to keep for this job
        :param pulumi.Input[str] project_id: ID of the project in which the backup exists
        :param pulumi.Input[str] schedule: Schedule for the backup, defined using restricted subset of cron
        :param pulumi.Input[str] source_cluster_id: the ID of the cluster to back up
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledBackupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ScheduledBackup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ScheduledBackupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledBackupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_description: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_backup_count: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 source_cluster_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ScheduledBackupArgs.__new__(ScheduledBackupArgs)

            if backup_description is None and not opts.urn:
                raise TypeError("Missing required property 'backup_description'")
            __props__.__dict__["backup_description"] = backup_description
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if max_backup_count is None and not opts.urn:
                raise TypeError("Missing required property 'max_backup_count'")
            __props__.__dict__["max_backup_count"] = max_backup_count
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if schedule is None and not opts.urn:
                raise TypeError("Missing required property 'schedule'")
            __props__.__dict__["schedule"] = schedule
            if source_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_cluster_id'")
            __props__.__dict__["source_cluster_id"] = source_cluster_id
        super(ScheduledBackup, __self__).__init__(
            'eventstorecloud:index/scheduledBackup:ScheduledBackup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_description: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            max_backup_count: Optional[pulumi.Input[int]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            source_cluster_id: Optional[pulumi.Input[str]] = None) -> 'ScheduledBackup':
        """
        Get an existing ScheduledBackup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_description: backup_description
        :param pulumi.Input[str] description: Human readable description of the job
        :param pulumi.Input[int] max_backup_count: The maximum number of backups to keep for this job
        :param pulumi.Input[str] project_id: ID of the project in which the backup exists
        :param pulumi.Input[str] schedule: Schedule for the backup, defined using restricted subset of cron
        :param pulumi.Input[str] source_cluster_id: the ID of the cluster to back up
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScheduledBackupState.__new__(_ScheduledBackupState)

        __props__.__dict__["backup_description"] = backup_description
        __props__.__dict__["description"] = description
        __props__.__dict__["max_backup_count"] = max_backup_count
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["source_cluster_id"] = source_cluster_id
        return ScheduledBackup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupDescription")
    def backup_description(self) -> pulumi.Output[str]:
        """
        backup_description
        """
        return pulumi.get(self, "backup_description")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Human readable description of the job
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="maxBackupCount")
    def max_backup_count(self) -> pulumi.Output[int]:
        """
        The maximum number of backups to keep for this job
        """
        return pulumi.get(self, "max_backup_count")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        ID of the project in which the backup exists
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[str]:
        """
        Schedule for the backup, defined using restricted subset of cron
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="sourceClusterId")
    def source_cluster_id(self) -> pulumi.Output[str]:
        """
        the ID of the cluster to back up
        """
        return pulumi.get(self, "source_cluster_id")

