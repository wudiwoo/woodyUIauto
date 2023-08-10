import jenkins

def configure_jenkins(report_directory, report_files):
    jenkins_url = 'http://localhost:8080'
    username = 'admin'
    password = 'admin'
    job_name = 'myjob'

    # 连接到 Jenkins 实例
    server = jenkins.Jenkins(jenkins_url, username=username, password=password)

    # 获取作业配置
    job_config = server.get_job_config(job_name)

    # 更新作业配置
    new_config = job_config.replace(
        '<publishers>',
        f'''
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
        ''')

    # 更新作业配置
    server.reconfig_job(job_name, new_config)

    print('Jenkins job configuration updated successfully.')

if __name__ == '__main__':
    report_directory = 'reports'
    report_file = 'report_20210810_120000.html'
    configure_jenkins(report_directory, report_file)