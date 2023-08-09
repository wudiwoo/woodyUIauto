from selenium import webdriver

def get_web_driver(browser):
    """获取指定浏览器的 WebDriver"""
    # 读取驱动程序路径配置文件
    with open('driver_paths.txt', 'r') as f:
        lines = f.readlines()

    driver_paths = {}
    for line in lines:
        parts = line.strip().split(':')
        if len(parts) != 2:
            continue
        browser_name, driver_path = parts
        driver_paths[browser_name] = driver_path

    # 获取指定浏览器的驱动程序路径
    driver_path = driver_paths.get(browser)
    if driver_path is None:
        raise ValueError(f'No driver path found for browser: {browser}')

    # 根据浏览器类型创建 WebDriver
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(executable_path=driver_path, options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(executable_path=driver_path, options=options)
    elif browser == 'safari':
        return webdriver.Safari()
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        return webdriver.Edge(executable_path=driver_path, options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser}')