# my_project_stuent_info_sys
webapp cgi + apache + python 

## 描述

> 1. 目的：一个简单的cgi练习项目
> 2. 工具：```python2.7```, ```apache-tomcat7```，```mySQL```
> 3. 内容：登录、注册功能
> 4. 路径：该项目位于apache webapp路径下

## web.xml、context.xml文件修改点
1. cgi servelet
```bash
 <servlet> # 取消该部分注释
        <servlet-name>cgi</servlet-name>
        <servlet-class>org.apache.catalina.servlets.CGIServlet</servlet-class>
        <init-param>
          <param-name>cgiPathPrefix</param-name>
          <param-value>WEB-INF/cgi</param-value>
        </init-param>
        
        <init-param>
          <param-name>executable</param-name>
          <param-value>C:/Python/Python27/python.exe</param-value> #  这个要改为自己的python解释器路径
        </init-param>
        <load-on-startup>5</load-on-startup>
</servlet>
```
2. conf -> context.xml
```python
<Context privileged="true"> # 添加属性privileged="true"
```
