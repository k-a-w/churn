End-to-End Customer Churn Analysis

Goals: in order to explain, predict, and classify customer churn for a large corporate dataset.

Following along with video

Added pip install python-dotenv for aws_connection.py



Notes to self:
    * Ask about the read_csv() method in aws_storage.py
    * Update docstrings
        * Most likely need to fix docstrings where :param was in there since I put additional comments instead of typing exactly what's on GitHub
        * Reword description for class TelcoEstimator in s3_estimator
    * Look in documentation to see what the convention is for spaces between a parameter and the default parameter (i.e. space or no space). I've used both in code so         standardize after determining what should be done.
    * Would like to research if the method name and class can be pulled into logging messages.
        May make it easier to log entering and exiting (can create additional messages in
        the constants \__init__.py folder?) but not sure if this could cause issues so the
        hard coding may make more sense.
        --Would it be feasible to play around with using \.__name__ and decorators?
            --Relevant StackOverflow Discussion:
            https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string

For keeping track of coding line lengths:
        
#Max recommended lengths of code (79 and 72 for docstrings)
###############################################################################
########################################################################
