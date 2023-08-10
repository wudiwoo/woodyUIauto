import requests
import xml.etree.ElementTree as ET

def configure_jenkins(report_directory, report_files):
    jenkins_url = 'http://localhost:8080'
    username = 'admin'
    password = 'admin'
    job_name = 'myUI'

    # 构建 Jenkins 配置 XML
    config_xml = f'''
    <project>
        <actions/>
        <description>My Jenkins Job</description>
        <keepDependencies>false</keepDependencies>
        <properties/>
        <scm class="hudson.scm.NullSCM"/>
        <canRoam>true</canRoam>
        <disabled>false</disabled>
        <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
        <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
        <triggers class="vector"/>
        <concurrentBuild>false</concurrentBuild>
        <builders/>
        <publishers>
            <hudson.plugins.htmlpublisher.HtmlPublisher>
                <reportTargets>
                    <hudson.plugins.htmlpublisher.HtmlPublisherTarget>
                        <reportName>My Report</reportName>
                        <reportDir>{report_directory}</reportDir>
                        <reportFiles>{report_files}</reportFiles>
                        <keepAll>true</keepAll>
                        <allowMissing>false</allowMissing>
                        <wrapperName>htmlpublisher-wrapper.html</wrapperName>
                    </hudson.plugins.htmlpublisher.HtmlPublisherTarget>
                </reportTargets>
            </hudson.plugins.htmlpublisher.HtmlPublisher>
        </publishers>
        <buildWrappers/>
    </project>
    '''

    # 发送 API 请求来更新 Jenkins 作业配置
    auth = (username, password)
    headers = {'Content-Type': 'application/xml'}
    url = f'{jenkins_url}/job/{job_name}/config.xml'
    response = requests.post(url, auth=auth, headers=headers, data=config_xml)
    if response.status_code == 200:
        print('Jenkins job configuration updated successfully.')
    else:
        print('Failed to update Jenkins job configuration.')

if __name__ == '__main__':
    report_directory = 'reports'
    report_file = 'report_20210810_120000.html'
    configure_jenkins(report_directory, report_file)