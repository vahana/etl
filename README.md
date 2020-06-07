# ETL Server

This is a demo server showcasing how to use [prf](https://github.com/vahana/prf), [datasets]([GitHub - vahana/prf: pyramid rest framework](https://github.com/vahana/prf)) and [jobs](https://github.com/vahana/jobs) libraries to build a ETL RESTful service.
It exposes end points to submit, monitor and collect ETL jobs using various database backends and Redis as job queue backend.
It is built using PRF framework, which in turn is based on Pyramid.

## PRF framework

PRF is a pyramid Restful Framework, that makes bootstraping, defining and processing RESTful endpoints generic, declarative and simplified. It supports various database backends, json payloads and RESTful resource tree declarations (e.g. nested resources). 
See [prf](https://github.com/vahana/prf) repo for more info.

## Datasets

Datasets is an abstraction over various data backends making managing and moving data around and between the backends transparent.
It is used here to support ETL pipelines between different backends seamless and uniform. 
See [datasets](https://github.com/vahana/datasets) repo for more info.

## Jobs

Jobs is a library used to define and queue jobs with batching, scheduling. It exposes RESTful endpoints to create and monitor jobs.
See [jobs](https://github.com/vahana/jobs) repo for more info.
