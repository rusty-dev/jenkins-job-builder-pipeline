## jenkins-job-builder-pipeline

A plugin for [jenkins-job-builder](http://docs.openstack.org/infra/jenkins-job-builder) to support [pipeline](https://wiki.jenkins-ci.org/display/JENKINS/Pipeline+Plugin) job generation.

Build Status: [![Build Status](https://travis-ci.org/rusty-dev/jenkins-job-builder-pipeline.svg)](https://travis-ci.org/rusty-dev/jenkins-job-builder-pipeline)

#### Usage:

Plugin adds a new project-type `pipeline` and a job definition field `pipeline`.
There are two distinct job definitions.

Create a pipeline job with a DSL script:
```yaml
- job:
    name: example-script
    project-type: pipeline
    pipeline:
      script: |
        # Your dsl script goes here.
        node {
          echo 'Hello world'
        }
      sandbox: true # Use groovy sandbox, false by default.
```
Create a pipeline job loading pipeline script from SCM.
```yaml
- job:
    name: example-scm-script
    project-type: pipeline
    pipeline:
      scriptPath: subdir/Jenkinsfile # path to pipeline script definition, "Jenkinsfile" by default.
      scm: # normal scm definitions
        - git:
            branches:
              - '*/maser'
            url: 'git@github.com:github-username/repository-name.git'
            basedir: 'subdir'
            skip-tag: true
            wipe-workspace: false

```

Definition type is chosen automatically by detecting presence of "scm" field.
