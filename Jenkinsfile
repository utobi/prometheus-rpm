#!/usr/bin/env groovy

node() {
    try {
        def folders = ["alertmanager", "graphite_exporter", "jmx_exporter", "jmx_javaagent_exporter", "node_exporter", "prometheus", "pushgateway"]

        stage 'Checkout Source'
        checkout scm

        for(String folder : folders) {
            dir(folder) {
                stage "Build "+folder
                sh 'make rpm'

                stage "Deploy "+folder
                withEnv(["FOO=BAR"]) {
                    echo "make deploy here..."
                    //sh 'make deploy'
                }
            }
        }
    } catch (err) {
        println "Build failed due to an error!"
        println err
        //todo emit slack msg
        currentBuild.result = "FAILURE"
    }
}
