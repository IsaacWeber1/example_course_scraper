from scraper_module.config import *

config = SpiderConfig(
    name="adams",
    start_url="https://adams.catalog.acalog.com/content.php?catoid=65&navoid=4154",
    use_playwright=False,
    tasks=[
        DynamicFind(
            task_name="dynamic_courses",
            search_space='xpath://a[contains(@href, "preview_course_nopop.php")]',
            base_url="https://adams.catalog.acalog.com/ajax/preview_course.php",
            catoid=65,
            fields={
                "title": 'xpath://h3//text()join',
                "description": 'xpath://div[2]/text()join'
            },
            pagination_selector='xpath://a[contains(@aria-label, "Page")]/@href'
        )
    ]
)