Installation
============

That sounds like a lot of work: `INSTALLATION`.
Don't worry, at Carries Cars we have tried to make on-boarding a pleasant experience.

 1. Clone the repository to a directory of choice;
 2. Open the directory in an IDE (e.g. [PyCharm][1] or [VS Code][2]);
 3. Verify that you are able to run the tests:
     - Navigate into the `money` module and run the tests
       ```bash
       $ cd money
       $ pytest 
       ```
     - Navigate into the `pricingEngine` module and run the tests
       ```bash
       $ cd pricingEngine
       $ pytest
       ```
 4. Configure the tests to run from your IDE:
     - **PyCharm**: 
       1. Open project in the IDE
       2. Open Preferences->Tools->Python Integrated Tools
       3. Under default test runner change to pytest
       4. Close preferences
       5. Right mouse button click on the test file test_money.py or test_pricing_engine,py in the project tree
       6. Select Run 'pytest in test_money' or 'Run 'pytest in test_pricing_engine' from the menu
       7. Inspect the results in the bottom pane (you should see ✅ Test Results)
     - **VS Code**: <not yet researched>

Frequently Asked Questions
--------------------------

 * **Do I really _need_ to use an IDE?**
   The short answer is yes. This workshop is build around the idea that the IDE can do a lot of the heavy lifting for us 
   when we start refactoring. During the workshop I recommend that you always use the IDE to change names of variables, 
   types, etc. By having the IDE take care of that we allow our brains to focus on the domain. Do make sure you run the
   tests each time you have made a change. Also in that regard I recommend running tests from within the IDE. This will 
   make navigation to test failures a lot quicker.  
   
   Certainly there are people that have vim set-up in ways that it can do a crazy amount of 
   heavy lifting too but that requires an awful lot of work. Those set-ups tend to be highly personalized making them 
   less ideal for collaboration because they require knowledge about the set-up.
 
 * **Do I really _need_ to run the test from within the IDE?**
   In my experience it is easier to navigate to the failing line of (test) code when you run the tests from within your 
   IDE. Take this workshop as an opportunity to experience a different way of working. It also allows you to easily run 
   a single test instead of the whole suite. Yes, I know, you can do that from the command line too but the barrier will
   always be slightly higher than with a simple button next to the test itself. 

 * **It's not working?! Help!**
   Please open an issue with a clear description:
    - Which steps you took
    - What the expected results were
    - What you got in stead
   Thank you for you help in improving this experience for those that will follow in your footsteps :-)