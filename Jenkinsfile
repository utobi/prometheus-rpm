#!/usr/bin/env groovy

folders = ["alertmanager", "graphite_exporter", "jmx_exporter", "jmx_javaagent_exporter", "node_exporter", "prometheus", "pushgateway"]

node() {
    try {
        stage 'Checkout Source'
        checkout scm

        withCredentials([[$class: 'UsernamePasswordBinding', credentialsId: "${env.DEPLOY_CREDENTIALS_ID}", variable: 'nexus_repository_credentials']]) {
            withEnv(["REPOSITORY_CREDENTIALS=${env.nexus_repository_credentials}"]) {

                for (String folder : folders) {
                    dir(folder) {
                        stage "Build " + folder
                        sh "make rpm"

                        stage "Deploy " + folder
                        sh "make deploy"
                    }
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
