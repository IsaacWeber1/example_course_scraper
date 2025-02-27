from scraper_module.config import *

config = SpiderConfig(
    name="brown_university",
    start_url="https://bulletin.appstate.edu/content.php?catoid=31&catoid=31&navoid=1925&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter",
    use_playwright=False,
    pagination=Search_Links(
        search_space='xpath://td[@class="block_content"]',
        link_selector='xpath:table/tbody/tr/td[@class="width"]/a',
        target_page_selector='xpath://div[@id="tabs"]/ul/li[@id="courseinventorytab"]/a/@href' # Target page to scrape
    ),
    tasks=[
        Find(
            task_name="courses",
            search_space='xpath://*[@id="courseinventorycontainer"]/div/div',
            repeating_selector="div",
            fields={
                "title": 'xpath:p[@class="courseblocktitle"]/strong//text()',
                "description": 'xpath:p[@class="courseblockdesc"]//text()join'
            },
            num_required=1
        )
    ]
)