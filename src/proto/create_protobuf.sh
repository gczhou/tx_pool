#!/bin/bash
protoc blockchain.proto --python_out .
protoc communication.proto --python_out .
protoc request.proto --python_out .
#case "$OSTYPE" in
#    darwin*)  
#        sed -ig 's/    result: ::std::option::Option<Response_oneof_result>,/    pub result: ::std::option::Option<Response_oneof_result>,/g' request.rs
#        sed -ig 's/    req: ::std::option::Option<Request_oneof_req>,/    pub req: ::std::option::Option<Request_oneof_req>,/g' request.rs
#        ;; 
#    *)       
#        sed -i 's/    result: ::std::option::Option<Response_oneof_result>,/    pub result: ::std::option::Option<Response_oneof_result>,/g' request.rs
#        sed -i 's/    req: ::std::option::Option<Request_oneof_req>,/    pub req: ::std::option::Option<Request_oneof_req>,/g' request.rs
#        ;;
#esac
protoc auth.proto --python_out .
