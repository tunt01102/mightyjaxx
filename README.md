<<<<<<< HEAD
# mightyjaxx
This is automation for mightyjaxx
=======
>>>>>>> 81b5349 (Add new project files)
#Last Update time: Sun 27 Oct, 2024
**1. Project Structure**

    ├── common/                # Common utilities and pre-steps for reuse
    │   ├── pre_steps.py       # Pre-test setup tasks like browser setup
    │   └── utils.py           # Utility functions like date formatting, logging
    ├── config/                # Configuration files
    │   └── environment.py     # Environment configurations (browser, headless mode, URLs, credentials, etc.)
    ├── evidences/             # Evidence storage for screenshots and logs
    │   └── YYYYMMDD/          # Auto-created subfolder for each test run (e.g., 20231024/)    
    ├── pages/                 # Page Object Model (POM) for different pages
    │   ├── base_page.py       # Base Page class with shared functions
    │   ├── home_page.py       # Home page with specific locators and actions
    │   ├── about_us_page.py   # About Us page with specific locators and actions
    │   └── blogs_page.py      # Blogs page with specific locators and actions
    ├── test_data/             # Test data for various features and pages
    │   ├── data_about_us.py   # Test data for the About Us page
    │   ├── data_blogs.py      # Test data for the Blogs page
    │   └── data_home.py       # Test data for the Home page
    ├── tests/                 # Test cases for various features and pages
    │   ├── test_about_us.py   # Test cases for the About Us page
    │   ├── test_blogs.py      # Test cases for the Blogs page
    │   └── test_home.py       # Test cases for the Home page
    ├── import_all.py          # Single file for importing all common modules and utils
    ├── README.md              # Documentation for the project
    ├── requirements.txt       # List of required packages
    └── main.py                # Entry point for running tests

**2. Setup and Installation**

    2.1. Clone the Repository: 
            COMMAND: git clone https://github.com/tunt01102/mightyjaxx.com.git
    2.2. Install Dependencies: Ensure you have Python installed, and install dependencies from requirements.txt
            COMMAND: pip install -r requirements.txt
    2.3. Install Playwright Browsers: Install Playwright and its required browser binaries.
            COMMAND: playwright install

**3. Configuring Test Parameters**

    Configurations are managed in the config/config.py file. Key parameters include:
    BROWSER: Choose between "chromium", "firefox", or "webkit".
    HEADLESS: Set to True for headless mode, or False to display the browser UI.
    WIDTH and HEIGHT: Set the browser viewport size.
    To change settings, edit config/environment.py

**4. Writing Tests**
    
    Tests are stored in the testcases/ directory. Here’s an example test flow:
    Pre-Test Setup: Initializes browser configurations and pre-conditions.
    Page Actions: Calls functions from Page Object Models (pages/ directory).
    Assertions: Verifies page elements and states.

**5. Utilities and Common Functions**
    
    Common utilities are stored in the common/ folder:
    pre_steps.py: Prepares the browser and context, dismisses popups, and instantiates page objects.
    utils.py: Helper functions for handling date formatting, logging, etc.

**6. Contributing**
    
    Fork the repository.
    Create a new branch for your feature or bug fix.
    Submit a pull request with a detailed description of your changes.
