
import random

class QuizBrain:
    
    def __init__(self):
        
        self._question_sets = [
            self._create_practitioner_learning_path(), # Practitioner questions
            self._create_developer_learning_path(),  # Developer questions
            self._create_question_set_one(),      # Original questions
            self._create_question_set_two(),      # Intermediate questions
            self._create_question_set_three()    # Advanced/Technical questions
            
        ]

    def _create_practitioner_learning_path(self):
    
        return [
            {
                "category": "Customer Engagement",
                "question": "What is the primary purpose of Braze as a platform?",
                "options": {
                    "A": "To reduce marketing costs",
                    "B": "To enable meaningful, data-informed customer engagement",
                    "C": "To create complex database structures",
                    "D": "To replace human marketers with AI"
                },
                "correct": "B"
            },
            {
                "category": "Customer Engagement",
                "question": "According to Braze, what is a key shift in marketing approach that their platform enables?",
                "options": {
                    "A": "From digital to print marketing",
                    "B": "From personalized to mass marketing",
                    "C": "From mass marketing to authentic, personalized interactions",
                    "D": "From customer engagement to data acquisition"
                },
                "correct": "C"
            },
            {
                "category": "Data Management",
                "question": "What is one of Braze's primary strengths related to data?",
                "options": {
                    "A": "Creating complex data visualizations",
                    "B": "Ingesting and unifying vast amounts of customer data from various sources",
                    "C": "Replacing a company's data warehouse",
                    "D": "Permanently storing all historical customer data"
                },
                "correct": "B"
            },
            {
                "category": "First-Party Data",
                "question": "Why is first-party data important for customer engagement according to Braze?",
                "options": {
                    "A": "It's cheaper than third-party data",
                    "B": "It allows for better understanding of customers and more personalized experiences",
                    "C": "It's the only legal form of data collection",
                    "D": "It provides information about competitors"
                },
                "correct": "B"
            },
            {
                "category": "User Profiles",
                "question": "What is a 'user profile' in Braze?",
                "options": {
                    "A": "A social media account connected to Braze",
                    "B": "A comprehensive view of an individual user that stores all persistent data about them",
                    "C": "A customer support ticket",
                    "D": "A marketing persona template"
                },
                "correct": "B"
            },
            {
                "category": "User Profiles",
                "question": "What types of information can be stored in a Braze user profile?",
                "options": {
                    "A": "Only basic contact information",
                    "B": "Only purchase history",
                    "C": "Only app usage data",
                    "D": "Behaviors, campaign interactions, personal characteristics, device information, and more"
                },
                "correct": "D"
            },
            {
                "category": "Segmentation",
                "question": "What is a segment in Braze?",
                "options": {
                    "A": "A portion of your app's user interface",
                    "B": "A type of message that can be sent to users",
                    "C": "A dynamic group of users targeted based on characteristics and actions",
                    "D": "A report showing user engagement"
                },
                "correct": "C"
            },
            {
                "category": "Segmentation",
                "question": "What makes Braze segments 'dynamic'?",
                "options": {
                    "A": "They can only be created by data scientists",
                    "B": "User membership changes in real-time as users interact with your app or website",
                    "C": "They only include active users",
                    "D": "They change automatically every 24 hours"
                },
                "correct": "B"
            },
            {
                "category": "Action-Based Messaging",
                "question": "What is 'action-based messaging' in Braze?",
                "options": {
                    "A": "Messages that require users to take action",
                    "B": "Messages that are sent in response to specific user actions on your app or website",
                    "C": "Messages that promote app features",
                    "D": "Messages that automatically perform actions"
                },
                "correct": "B"
            },
            {
                "category": "Real-Time Decisioning",
                "question": "How does real-time decisioning benefit customer engagement?",
                "options": {
                    "A": "It reduces the need for marketing staff",
                    "B": "It allows instant interaction with users at the exact moment they're engaging with your brand",
                    "C": "It eliminates the need for segmentation",
                    "D": "It makes all messaging automated"
                },
                "correct": "B"
            },
            {
                "category": "Personalization",
                "question": "What is 'Liquid' in Braze?",
                "options": {
                    "A": "A visual design tool",
                    "B": "A template language used to dynamically insert user data into messages",
                    "C": "A fluid messaging interface",
                    "D": "A database management system"
                },
                "correct": "B"
            },
            {
                "category": "Personalization",
                "question": "What is dynamic content in Braze?",
                "options": {
                    "A": "Content that changes based on who is interacting with it",
                    "B": "Videos that play automatically",
                    "C": "Content created by AI",
                    "D": "Messages that change daily"
                },
                "correct": "A"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "According to Braze research, by what percentage can cross-channel strategies increase a user's average lifetime?",
                "options": {
                    "A": "25%",
                    "B": "50%",
                    "C": "76%",
                    "D": "100%"
                },
                "correct": "C"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "Which of these is classified as an 'out-of-product' channel in Braze?",
                "options": {
                    "A": "Content Cards",
                    "B": "In-App Messages",
                    "C": "Email",
                    "D": "Website popups"
                },
                "correct": "C"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "Which of these is classified as an 'in-product' channel in Braze?",
                "options": {
                    "A": "SMS",
                    "B": "Email",
                    "C": "Web Push",
                    "D": "Content Cards"
                },
                "correct": "D"
            },
            {
                "category": "Canvas",
                "question": "What is Braze Canvas?",
                "options": {
                    "A": "A graphic design tool",
                    "B": "A visual journey orchestration tool for designing customer journeys",
                    "C": "A reporting dashboard",
                    "D": "A user interface template"
                },
                "correct": "B"
            },
            {
                "category": "Canvas",
                "question": "What is journey orchestration in Braze?",
                "options": {
                    "A": "Creating email sequences",
                    "B": "Assigning tasks to team members",
                    "C": "The process of designing, managing, and optimizing customer journeys across touchpoints",
                    "D": "Scheduling content publication"
                },
                "correct": "C"
            },
            {
                "category": "Canvas",
                "question": "Which feature in Canvas allows you to evaluate the effectiveness of different campaign variations?",
                "options": {
                    "A": "Personalization",
                    "B": "Multi-Channel Engagement",
                    "C": "Automation and Triggers",
                    "D": "Experimentation"
                },
                "correct": "D"
            },
            {
                "category": "Customer Data",
                "question": "How does Braze conceptualize customers compared to traditional database approaches?",
                "options": {
                    "A": "As segments rather than individuals",
                    "B": "As leads rather than customers",
                    "C": "As individuals rather than lines in a database",
                    "D": "As prospects rather than users"
                },
                "correct": "C"
            },
            {
                "category": "Customer Engagement",
                "question": "What can be triggered using data from a user profile in Braze?",
                "options": {
                    "A": "Only scheduled campaigns",
                    "B": "Action-based messages, personalized content, and user segmentation",
                    "C": "Only push notifications",
                    "D": "Only customer service interactions"
                },
                "correct": "B"
            },
            {
                "category": "Personalization",
                "question": "What benefits does dynamic content provide according to the Braze learning path?",
                "options": {
                    "A": "Lower messaging costs",
                    "B": "Faster delivery times",
                    "C": "Improved efficiency, engagement, and conversion rates",
                    "D": "Reduced need for creative content"
                },
                "correct": "C"
            },
            {
                "category": "Segmentation",
                "question": "What do Braze segment analytics features enable?",
                "options": {
                    "A": "Creation of new segments",
                    "B": "Precise performance reports and analytics based on specific segments",
                    "C": "Automatic message sending",
                    "D": "User profile updates"
                },
                "correct": "B"
            },
            {
                "category": "Canvas",
                "question": "How does Canvas respond to user actions during a journey?",
                "options": {
                    "A": "It ignores them until the journey is complete",
                    "B": "It actively listens and adjusts the user's path based on their actions",
                    "C": "It pauses the journey until manual review",
                    "D": "It can only follow pre-set paths regardless of user actions"
                },
                "correct": "B"
            },
            {
                "category": "Canvas",
                "question": "What capability does Canvas provide for abandoned cart scenarios?",
                "options": {
                    "A": "Automatic price matching with competitors",
                    "B": "Creation of a multi-step, multi-channel journey to encourage purchase completion",
                    "C": "Automatic cart deletion after 24 hours",
                    "D": "Manual follow-up by sales team"
                },
                "correct": "B"
            },
            {
                "category": "Data Integration",
                "question": "What is the benefit of Braze's ability to ingest real-time event data?",
                "options": {
                    "A": "It reduces database size",
                    "B": "It enables real-time responsive messaging based on user actions",
                    "C": "It eliminates the need for a data warehouse",
                    "D": "It automatically generates reports"
                },
                "correct": "B"
            },
            {
                "category": "Personalization",
                "question": "In the Braze example of a fitness app, what type of data was used to personalize messages?",
                "options": {
                    "A": "Only demographic information",
                    "B": "Only purchase history",
                    "C": "Workout preferences and frequency",
                    "D": "Only login times"
                },
                "correct": "C"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "What is a key advantage of combining multiple channels in a messaging strategy?",
                "options": {
                    "A": "It reduces the total number of messages sent",
                    "B": "It provides multiple touchpoints to reinforce your message",
                    "C": "It eliminates the need for segmentation",
                    "D": "It always guarantees higher conversion rates"
                },
                "correct": "B"
            },
            {
                "category": "Customer Engagement",
                "question": "According to the Braze learning path, what is an essential element of customer engagement?",
                "options": {
                    "A": "Sending as many messages as possible",
                    "B": "Using only the newest channels",
                    "C": "Creating relevant conversations that guide users through customer-centered journeys",
                    "D": "Focusing exclusively on acquisition rather than retention"
                },
                "correct": "C"
            },
            {
                "category": "Personalization",
                "question": "What can the personalization modal in Braze's message composer help you add?",
                "options": {
                    "A": "Only images",
                    "B": "Liquid personalization to your message",
                    "C": "Only emoji reactions",
                    "D": "Only countdown timers"
                },
                "correct": "B"
            },
            {
                "category": "Canvas",
                "question": "What is one of the AI capabilities mentioned for Canvas?",
                "options": {
                    "A": "Automatic content creation",
                    "B": "Customer support chatbots",
                    "C": "Measuring journey effectiveness and optimizing messaging",
                    "D": "Predicting customer lifetime value"
                },
                "correct": "C"
            }
        ]
    
    def _create_developer_learning_path(self):
        
        return [
            {
                "category": "Braze Fundamentals",
                "question": "What is Braze primarily described as in the learning materials?",
                "options": {
                    "A": "A social media management platform",
                    "B": "A customer engagement platform or CRM tool",
                    "C": "A data warehouse solution",
                    "D": "An email marketing service"
                },
                "correct": "B"
            },
            {
                "category": "Braze Fundamentals",
                "question": "What key capability does Braze provide to marketers?",
                "options": {
                    "A": "The ability to design new apps and websites",
                    "B": "The ability to collect third-party data without consent",
                    "C": "The ability to create personalized customer experiences with minimal technical assistance",
                    "D": "The ability to replace engineering teams with AI"
                },
                "correct": "C"
            },
            {
                "category": "Data Management",
                "question": "What types of data does Braze primarily focus on?",
                "options": {
                    "A": "Third-party and purchased data",
                    "B": "Competitor analysis data",
                    "C": "Zero-party and first-party data",
                    "D": "Public social media data"
                },
                "correct": "C"
            },
            {
                "category": "Data Management",
                "question": "How does Braze handle real-time data processing?",
                "options": {
                    "A": "It processes data once per day in batches",
                    "B": "It can ingest data and send messages in just over a second",
                    "C": "It requires manual processing by marketers",
                    "D": "It only processes data on weekdays"
                },
                "correct": "B"
            },
            {
                "category": "Tech Integration",
                "question": "What is required to enable in-app messages and content cards in Braze?",
                "options": {
                    "A": "A separate messaging service",
                    "B": "SDK integration into your apps and websites",
                    "C": "Custom HTML development for each message",
                    "D": "A special subscription tier"
                },
                "correct": "B"
            },
            {
                "category": "Developer Roles",
                "question": "What are the two main tasks that typically require developer support during Braze onboarding?",
                "options": {
                    "A": "User training and dashboard setup",
                    "B": "Message design and campaign creation",
                    "C": "SDK integration and REST API configuration",
                    "D": "Database migration and server provisioning"
                },
                "correct": "C"
            },
            {
                "category": "Data Types",
                "question": "What are the four basic categories of data in Braze?",
                "options": {
                    "A": "Personal, behavioral, transactional, and demographic",
                    "B": "Automatically collected data, standard attributes, custom data, and purchase data",
                    "C": "User data, app data, message data, and conversion data",
                    "D": "Internal, external, structured, and unstructured"
                },
                "correct": "B"
            },
            {
                "category": "Data Types",
                "question": "What kind of data does Braze automatically collect when the SDK is initialized?",
                "options": {
                    "A": "Only user login information",
                    "B": "Only purchase history",
                    "C": "Session start/end, device data, geolocation, and message interaction data",
                    "D": "Only email addresses and phone numbers"
                },
                "correct": "C"
            },
            {
                "category": "Data Points",
                "question": "What is a 'data point' in Braze?",
                "options": {
                    "A": "A visual marker on analytics graphs",
                    "B": "A unit that measures each granular user action for billing purposes",
                    "C": "A connection between two databases",
                    "D": "A target goal for marketing campaigns"
                },
                "correct": "B"
            },
            {
                "category": "Data Points",
                "question": "Which of the following does NOT count toward your Braze data point allotment?",
                "options": {
                    "A": "Session start data",
                    "B": "Custom attributes",
                    "C": "Message interaction data (collected automatically)",
                    "D": "Custom events"
                },
                "correct": "C"
            },
            {
                "category": "Data Optimization",
                "question": "What is a key strategy for optimizing data point consumption?",
                "options": {
                    "A": "Sending all user data daily",
                    "B": "Only sending data that has changed (data deltas)",
                    "C": "Logging out users after each session",
                    "D": "Creating a new user profile for each device"
                },
                "correct": "B"
            },
            {
                "category": "User Profiles",
                "question": "What does a user profile in Braze represent?",
                "options": {
                    "A": "Only demographic information about a user",
                    "B": "Only a user's messaging preferences",
                    "C": "A collection of data representing an individual consumer and their behaviors",
                    "D": "Only purchase history information"
                },
                "correct": "C"
            },
            {
                "category": "User Profiles",
                "question": "What tools does Braze offer for viewing individual user profiles?",
                "options": {
                    "A": "Only API access",
                    "B": "Search Users tool and Segment User Data tool",
                    "C": "Only CSV exports",
                    "D": "Only automated reports"
                },
                "correct": "B"
            },
            {
                "category": "User Lifecycle",
                "question": "What is the typical user lifecycle in Braze?",
                "options": {
                    "A": "Created, active, dormant",
                    "B": "Anonymous, identified, possibly archived",
                    "C": "New, returning, churned",
                    "D": "Prospect, customer, advocate"
                },
                "correct": "B"
            },
            {
                "category": "User Identification",
                "question": "What function is used to identify a user in the Braze SDK?",
                "options": {
                    "A": "identifyUser()",
                    "B": "setUserID()",
                    "C": "changeUser()",
                    "D": "loginUser()"
                },
                "correct": "C"
            },
            {
                "category": "Anonymous Users",
                "question": "How does Braze track anonymous users?",
                "options": {
                    "A": "It doesn't track users until they register",
                    "B": "It assigns a unique braze_id to each device",
                    "C": "It uses cookies only",
                    "D": "It requires an email address"
                },
                "correct": "B"
            },
            {
                "category": "User Identification",
                "question": "What happens when an anonymous user becomes identified in Braze?",
                "options": {
                    "A": "Their anonymous data is deleted",
                    "B": "Their anonymous profile is merged with their new identified profile",
                    "C": "Their anonymous profile remains separate",
                    "D": "They start with a blank profile"
                },
                "correct": "B"
            },
            {
                "category": "User Aliases",
                "question": "What is the purpose of user aliases in Braze?",
                "options": {
                    "A": "To create backup copies of user profiles",
                    "B": "To store alternative names for display",
                    "C": "To add key-value pairs that persist on a profile and can be used for merging",
                    "D": "To hide user identities for privacy"
                },
                "correct": "C"
            },
            {
                "category": "User Archival",
                "question": "How are inactive users handled in Braze?",
                "options": {
                    "A": "They remain in the system indefinitely",
                    "B": "They are automatically archived on a weekly cadence",
                    "C": "They must be manually removed",
                    "D": "They are immediately deleted after 30 days"
                },
                "correct": "B"
            },
            {
                "category": "SDK Integration",
                "question": "What are the two main benefits of SDK integration with Braze?",
                "options": {
                    "A": "Lower costs and faster performance",
                    "B": "Better security and user privacy",
                    "C": "Real-time data flow and in-product messaging capabilities",
                    "D": "Simplified coding and reduced app size"
                },
                "correct": "C"
            },
            {
                "category": "REST API",
                "question": "What is the Braze REST API commonly used for?",
                "options": {
                    "A": "Only for testing campaigns",
                    "B": "Only for user authentication",
                    "C": "Importing historical data and communication between tech stack components",
                    "D": "Only for dashboard customization"
                },
                "correct": "C"
            },
            {
                "category": "Standard Attributes",
                "question": "What happens if you name a field 'date_of_birth' instead of 'dob' when submitting data to Braze?",
                "options": {
                    "A": "The data will be rejected",
                    "B": "Braze will automatically correct the field name",
                    "C": "It will create a custom attribute with that name instead of using the standard attribute",
                    "D": "The user profile will be duplicated"
                },
                "correct": "C"
            },
            {
                "category": "Custom Events",
                "question": "How long are custom event properties saved in Braze by default?",
                "options": {
                    "A": "Forever",
                    "B": "90 days",
                    "C": "30 days",
                    "D": "7 days"
                },
                "correct": "C"
            },
            {
                "category": "Purchase Data",
                "question": "Which of the following is a predefined field for purchase data in Braze?",
                "options": {
                    "A": "sale_amount",
                    "B": "item_name",
                    "C": "price",
                    "D": "transaction_id"
                },
                "correct": "C"
            },
            {
                "category": "Data Points",
                "question": "If your contract includes 1,000 MAU with 250 data points each, what would be your total data allotment for 1 year?",
                "options": {
                    "A": "250,000",
                    "B": "1,000,000",
                    "C": "3,000,000",
                    "D": "12,000,000"
                },
                "correct": "C"
            },
            {
                "category": "Session Data",
                "question": "What can you customize to reduce session data points?",
                "options": {
                    "A": "User identification method",
                    "B": "Session timeout length",
                    "C": "Data encryption level",
                    "D": "Campaign frequency"
                },
                "correct": "B"
            },
            {
                "category": "Data Management",
                "question": "What happens if you send a user's first_name multiple times with the same value?",
                "options": {
                    "A": "Only the first submission counts as a data point",
                    "B": "Only the most recent submission counts as a data point",
                    "C": "Each submission counts as a separate data point",
                    "D": "None count as data points since the value didn't change"
                },
                "correct": "C"
            },
            {
                "category": "Web Integration",
                "question": "What is a potential concern with session data on web implementations?",
                "options": {
                    "A": "Session data isn't collected on web",
                    "B": "Web sessions use more data points than mobile sessions",
                    "C": "Anonymous web visitors could consume many data points during traffic spikes",
                    "D": "Web sessions can't be tracked across browser tabs"
                },
                "correct": "C"
            },
            {
                "category": "Tech Integration",
                "question": "How does Braze typically fit into an organization's tech stack?",
                "options": {
                    "A": "It replaces all other marketing tools",
                    "B": "It integrates with existing platforms and tools to complement what they do",
                    "C": "It operates completely independently of other systems",
                    "D": "It only works with specific proprietary systems"
                },
                "correct": "B"
            },
            {
                "category": "Data Export",
                "question": "What feature does Braze provide for exporting data to external systems?",
                "options": {
                    "A": "Manual CSV download only",
                    "B": "Braze Currents",
                    "C": "Email attachments",
                    "D": "Periodic snapshots"
                },
                "correct": "B"
            }
        ]

    def _create_question_set_one(self):
        
        # Return the original question set (already in your code)
        return [
            {
                "category": "Segmentation",
                "question": "What is the main use of audience segmentation in Braze?",
                "options": {
                    "A": "Reducing database size",
                    "B": "Creating personalized user experiences through targeting",
                    "C": "Sending bulk messages to all users",
                    "D": "Randomly grouping users"
                },
                "correct": "B"
            },
            {
                "category": "Segmentation",
                "question": "Which of the following is a valid segmentation filter operator in Braze?",
                "options": {
                    "A": "Roughly matches",
                    "B": "Exactly",
                    "C": "Partially contains",
                    "D": "Mimics"
                },
                "correct": "B"
            },
            {
                "category": "Segmentation",
                "question": "What does the AND NOT operator do in a segment setup?",
                "options": {
                    "A": "Adds another filter",
                    "B": "Excludes a user group from the target segment",
                    "C": "Duplicates a segment",
                    "D": "Combines two segments"
                },
                "correct": "B"
            },
            {
                "category": "Campaigns & Canvases",
                "question": "Which delivery method allows a campaign to be triggered by a specific event, such as a user action?",
                "options": {
                    "A": "Schedule-based",
                    "B": "Action-based",
                    "C": "Export-based",
                    "D": "Recurring"
                },
                "correct": "B"
            },
            {
                "category": "Campaigns & Canvases",
                "question": "How many variants can you use for A/B testing in a single Braze campaign?",
                "options": {
                    "A": "4",
                    "B": "6",
                    "C": "8",
                    "D": "10"
                },
                "correct": "C"
            },
            {
                "category": "Campaigns & Canvases",
                "question": "What is a benefit of using Canvases over single Campaigns?",
                "options": {
                    "A": "They're easier to set up",
                    "B": "They allow full customer journey orchestration",
                    "C": "They only support push notifications",
                    "D": "They don't require data tracking"
                },
                "correct": "B"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "Which of the following is considered an out-of-product channel in Braze?",
                "options": {
                    "A": "Push Notifications",
                    "B": "Content Cards",
                    "C": "In-app messages",
                    "D": "In-browser messages"
                },
                "correct": "A"
            },
            {
                "category": "Cross-Channel Messaging",
                "question": "What's a best practice when building a cross-channel strategy?",
                "options": {
                    "A": "Use only one channel to reduce complexity",
                    "B": "Send identical messages across all channels",
                    "C": "Keep messaging consistent but tailored to the channel",
                    "D": "Avoid leveraging Canvas"
                },
                "correct": "C"
            },
            {
                "category": "Analytics & Reporting",
                "question": "Where do you view campaign performance metrics like unique recipients, conversion rate, and revenue?",
                "options": {
                    "A": "Segment Insights",
                    "B": "Campaign Analytics",
                    "C": "Retention Report",
                    "D": "Home Page"
                },
                "correct": "B"
            },
            {
                "category": "Analytics & Reporting",
                "question": "Which report helps you understand how users flow through a post-campaign journey?",
                "options": {
                    "A": "Global control group",
                    "B": "Funnel report",
                    "C": "Data usage dashboard",
                    "D": "Segment Insights"
                },
                "correct": "B"
            },
            {
                "category": "Analytics & Reporting",
                "question": "Which feature lets you create SQL-based custom analytics queries within Braze?",
                "options": {
                    "A": "Report Builder",
                    "B": "Query Builder",
                    "C": "Segment Builder",
                    "D": "Insight Engine"
                },
                "correct": "B"
            },
            {
                "category": "Analytics & Reporting",
                "question": "What does the Global Control Group report help measure?",
                "options": {
                    "A": "Push performance",
                    "B": "Messaging impact vs no messaging",
                    "C": "Email delivery failures",
                    "D": "Segmentation filters"
                },
                "correct": "B"
            },
            {
                "category": "Dashboard, Setup & Permissions",
                "question": "Which of the following can you configure under Braze's security settings?",
                "options": {
                    "A": "Authentication policies and IP allowlists",
                    "B": "Campaign templates",
                    "C": "Message styling rules",
                    "D": "Custom footers"
                },
                "correct": "A"
            },
            {
                "category": "Dashboard, Setup & Permissions",
                "question": "Which of these actions is NOT available in the 'Settings > Company Users' section?",
                "options": {
                    "A": "Adding new users",
                    "B": "Assigning roles",
                    "C": "Setting conversion events",
                    "D": "Granting admin privileges"
                },
                "correct": "C"
            },
            {
                "category": "Dashboard, Setup & Permissions",
                "question": "Which footer attribute must be included in emails for unsubscribe functionality?",
                "options": {
                    "A": "{{unsubscribe_url}}",
                    "B": "{{${email_unsubscribe_link}}}",
                    "C": "{{${set_user_to_unsubscribe_url}}}",
                    "D": "{{footer_link_unsubscribe}}"
                },
                "correct": "C"
            },
            {
                "category": "Data & Usage",
                "question": "Which of the following does NOT count toward Braze's data point allotment?",
                "options": {
                    "A": "Sending NULL values",
                    "B": "Sending blank values",
                    "C": "Uploading via CSV",
                    "D": "Custom attributes"
                },
                "correct": "B"
            },
            {
                "category": "Data & Usage",
                "question": "What feature helps reduce data point usage when enriching data in segments?",
                "options": {
                    "A": "Query Builder",
                    "B": "Segment Extensions and Connect Content",
                    "C": "CSV Import",
                    "D": "Funnel Reports"
                },
                "correct": "B"
            },
            {
                "category": "Data & Usage",
                "question": "What is a Workspace in Braze used for?",
                "options": {
                    "A": "A place to store user profiles",
                    "B": "A dedicated area for a brand/app with isolated data",
                    "C": "A message styling tool",
                    "D": "The campaign testing environment"
                },
                "correct": "B"
            },
            {
                "category": "Data Integration",
                "question": "Which Braze SDK method is used to identify a user with a unique ID?",
                "options": {
                    "A": "braze.logUser()",
                    "B": "braze.identifyUser()",
                    "C": "braze.changeUser()",
                    "D": "braze.setUserID()"
                },
                "correct": "C"
            },
            {
                "category": "Data Integration",
                "question": "What is the maximum number of custom attributes that can be stored for a single user profile in Braze?",
                "options": {
                    "A": "25",
                    "B": "50",
                    "C": "100",
                    "D": "Unlimited"
                },
                "correct": "C"
            },
            {
                "category": "API & Implementation",
                "question": "Which of the following is NOT a valid Braze REST API endpoint category?",
                "options": {
                    "A": "users/track",
                    "B": "campaigns/trigger",
                    "C": "messages/schedule",
                    "D": "segments/analytics"
                },
                "correct": "D"
            },
            {
                "category": "Canvas",
                "question": "What is the primary purpose of Canvas Entry Properties in Braze?",
                "options": {
                    "A": "To define when users can re-enter a Canvas",
                    "B": "To pass data to a Canvas that can be used for personalization",
                    "C": "To control which channels can be used in a Canvas",
                    "D": "To set expiration dates for Canvas messages"
                },
                "correct": "B"
            },
            {
                "category": "Canvas",
                "question": "Which Canvas component allows you to split users into different paths based on a random selection?",
                "options": {
                    "A": "Message step",
                    "B": "Action Paths",
                    "C": "Decision Split",
                    "D": "Distribution"
                },
                "correct": "D"
            },
            {
                "category": "Messaging",
                "question": "Which of the following liquid syntax would correctly display a user's first name, or 'there' if no first name is available?",
                "options": {
                    "A": "{{user.first_name|default:'there'}}",
                    "B": "{% if user.first_name %}{{user.first_name}}{% else %}there{% endif %}",
                    "C": "{{#if user.first_name}}{{user.first_name}}{{else}}there{{/if}}",
                    "D": "{{user.first_name || 'there'}}"
                },
                "correct": "A"
            },
            {
                "category": "Messaging",
                "question": "Which of these is a best practice for in-app message delivery in Braze?",
                "options": {
                    "A": "Always show the same message across all app sessions",
                    "B": "Set an impression cap to avoid overwhelming users",
                    "C": "Use Action-Based delivery for all in-app messaging",
                    "D": "Include at least 3 CTA buttons"
                },
                "correct": "B"
            },
            {
                "category": "Reporting & Analytics",
                "question": "Which of the following metrics is NOT available in the Campaign Analytics page?",
                "options": {
                    "A": "Unique recipients",
                    "B": "Lifetime value of recipients",
                    "C": "Direct opens",
                    "D": "Revenue per user"
                },
                "correct": "D"
            },
            {
                "category": "Reporting & Analytics",
                "question": "What does the 'Variation' column show in a Canvas Performance table?",
                "options": {
                    "A": "Different sets of message content being tested",
                    "B": "Different audience segments entering the Canvas",
                    "C": "Different steps within the Canvas journey",
                    "D": "Different conversion rates over time"
                },
                "correct": "A"
            },
            {
                "category": "User Data",
                "question": "What happens when a user's profile is merged in Braze?",
                "options": {
                    "A": "Only the most recent custom attributes are kept",
                    "B": "Only the most recent events are kept",
                    "C": "All data is preserved from both profiles",
                    "D": "Purchase history is deleted"
                },
                "correct": "C"
            },
            {
                "category": "User Data",
                "question": "Which of the following is NOT a standard user data field in Braze?",
                "options": {
                    "A": "Last name",
                    "B": "Email address",
                    "C": "Social media handles",
                    "D": "Country"
                },
                "correct": "C"
            },
            {
                "category": "Content Cards",
                "question": "What is a key advantage of using Content Cards over other messaging channels in Braze?",
                "options": {
                    "A": "They can only be viewed when online",
                    "B": "They require no user opt-in permissions",
                    "C": "They must be viewed in chronological order",
                    "D": "They cannot be personalized with user data"
                },
                "correct": "B"
            }
        ]    

    def _create_question_set_two(self):
        
        return [
            {
                "category": "Advanced Segmentation",
                "question": "What is the purpose of 'Nested Segments' in Braze?",
                "options": {
                    "A": "To create segments based on subscription status",
                    "B": "To combine multiple segment filters together",
                    "C": "To use one segment as a filter within another segment",
                    "D": "To exclude users from segmentation"
                },
                "correct": "C"
            },
            {
                "category": "Predictive Analytics",
                "question": "What is the purpose of Braze's Predictive Churn feature?",
                "options": {
                    "A": "To predict which users will spend the most money",
                    "B": "To identify users who are likely to uninstall your app or become inactive",
                    "C": "To forecast server load during peak periods",
                    "D": "To analyze past campaign performance"
            },
                "correct": "B"
            },
            {
                "category": "Advanced Segmentation",
                "question": "What is a Rolling Window in Braze segmentation?",
                "options": {
                    "A": "A time period that moves with the current date",
                    "B": "A popup window in the Braze dashboard",
                    "C": "A fixed date range for campaigns",
                    "D": "A type of Canvas component"
                },
                "correct": "A"
            },
            {
                "category": "Advanced Segmentation",
                "question": "Which of these can be used as a segmentation filter in Braze?",
                "options": {
                    "A": "User social media engagement",
                    "B": "Weather in user's location",
                    "C": "Purchase history from external systems via Segment Extensions",
                    "D": "Website bounce rate"
                },
                "correct": "C"
            },
            {
                "category": "Advanced Canvas",
                "question": "What is the purpose of the 'Audience Sync' step in Canvas Flow?",
                "options": {
                    "A": "To synchronize user profiles across apps",
                    "B": "To export audience data to external systems like Facebook or Google",
                    "C": "To create a backup of user data",
                    "D": "To combine multiple canvases"
                },
                "correct": "B"
            },
            {
                "category": "Advanced Canvas",
                "question": "What does the 'Experiment Paths' component allow you to do in Canvas Flow?",
                "options": {
                    "A": "Test new Canvas features",
                    "B": "Automatically optimize message delivery times",
                    "C": "Compare the performance of different customer journeys",
                    "D": "Randomize message content"
                },
                "correct": "C"
            },
            {
                "category": "Advanced Canvas",
                "question": "What is unique about the 'Message Step' in Canvas Flow compared to earlier Canvas versions?",
                "options": {
                    "A": "It can contain multiple channels in one step",
                    "B": "It can only send emails",
                    "C": "It requires manual approval",
                    "D": "It can only send to iOS devices"
                },
                "correct": "A"
            },
            {
                "category": "Personalization",
                "question": "What is Liquid used for in Braze?",
                "options": {
                    "A": "Creating dynamic content based on user attributes",
                    "B": "Designing mobile app interfaces",
                    "C": "Processing payments",
                    "D": "Managing database connections"
                },
                "correct": "A"
            },
            {
                "category": "Personalization",
                "question": "Which Liquid tag would you use to show content only to users who have made a purchase?",
                "options": {
                    "A": "{% if user.made_purchase == true %}",
                    "B": "{{ if: user.purchases > 0 }}",
                    "C": "{{ user.purchased? }}",
                    "D": "{% show_if purchased %}"
                },
                "correct": "A"
            },
            {
                "category": "Personalization",
                "question": "How can you use Braze's Connected Content to enhance personalization?",
                "options": {
                    "A": "By connecting to social media profiles",
                    "B": "By fetching real-time data from external APIs",
                    "C": "By enabling peer-to-peer messaging",
                    "D": "By creating custom HTML templates"
                },
                "correct": "B"
            },
            {
                "category": "Intelligent Timing",
                "question": "What does Intelligent Timing in Braze optimize for?",
                "options": {
                    "A": "Sending messages when server load is lowest",
                    "B": "Sending messages when users are most likely to engage",
                    "C": "Reducing the total number of messages sent",
                    "D": "Coordinating campaigns across teams"
                },
                "correct": "B"
            },
            {
                "category": "Intelligent Timing",
                "question": "What data does Intelligent Timing use to determine optimal send times?",
                "options": {
                    "A": "User's historical app usage patterns",
                    "B": "External market research",
                    "C": "Industry benchmarks",
                    "D": "Random sampling"
                },
                "correct": "A"
            },
            {
                "category": "Intelligent Timing",
                "question": "What happens if a user has no historical data for Intelligent Timing to analyze?",
                "options": {
                    "A": "The message is not sent",
                    "B": "The message is sent at a randomly selected time",
                    "C": "The message is sent at the campaign's designated fallback time",
                    "D": "The user is removed from the campaign"
                },
                "correct": "C"
            },
            {
                "category": "Advanced Messaging",
                "question": "What is a Push Story in Braze?",
                "options": {
                    "A": "A narrative-based push notification",
                    "B": "A series of connected push notifications",
                    "C": "A carousel of images and text within a single push notification",
                    "D": "A push notification with animated content"
                },
                "correct": "C"
            },
            {
                "category": "Advanced Messaging",
                "question": "What feature allows you to schedule recurring messages at custom intervals?",
                "options": {
                    "A": "Recurring campaigns",
                    "B": "Scheduled API triggers",
                    "C": "Canvas Journey Scheduler",
                    "D": "Cron-based delivery"
                },
                "correct": "A"
            },
            {
                "category": "Advanced Messaging",
                "question": "What is unique about Silent Push Notifications in Braze?",
                "options": {
                    "A": "They show no visible notification to the user",
                    "B": "They make no sound when delivered",
                    "C": "They can only contain text content",
                    "D": "They bypass notification settings"
                },
                "correct": "A"
            },
            {
                "category": "Content Cards",
                "question": "How can Content Cards be configured to display in a mobile app?",
                "options": {
                    "A": "Only as a full-page feed",
                    "B": "Only as individual cards",
                    "C": "As a feed, in a custom UI location, or programmatically",
                    "D": "Only in the app's notification center"
                },
                "correct": "C"
            },
            {
                "category": "Content Cards",
                "question": "What happens to Content Cards when a user's device is offline?",
                "options": {
                    "A": "They are lost and never displayed",
                    "B": "They are stored locally and displayed when the app opens",
                    "C": "They are queued on the server until reconnection",
                    "D": "They are converted to push notifications"
                },
                "correct": "B"
            },
            {
                "category": "Content Cards",
                "question": "Which of these is a unique advantage of Content Cards over other messaging channels?",
                "options": {
                    "A": "They can contain more rich media",
                    "B": "They remain available until explicitly dismissed or expired",
                    "C": "They don't require user permissions",
                    "D": "They can only be seen by premium users"
                },
                "correct": "B"
            },
            {
                "category": "Advanced Analytics",
                "question": "What is a Funnel Report used for in Braze?",
                "options": {
                    "A": "Analyzing sequential user actions after receiving a message",
                    "B": "Visualizing email delivery rates",
                    "C": "Monitoring server performance",
                    "D": "Tracking social media mentions"
                },
                "correct": "A"
            },
            {
                "category": "Advanced Analytics",
                "question": "What is the purpose of a Global Control Group in Braze?",
                "options": {
                    "A": "To test new features before release",
                    "B": "To measure the overall impact of your messaging by excluding some users from all campaigns",
                    "C": "To benchmark against industry standards",
                    "D": "To ensure compliance with regional regulations"
                },
                "correct": "B"
            },
            {
                "category": "Advanced Analytics",
                "question": "What can you track with custom events in Braze?",
                "options": {
                    "A": "Only pre-defined user actions",
                    "B": "Only purchase events",
                    "C": "Any user interaction or event that you define",
                    "D": "Only page views and clicks"
                },
                "correct": "C"
            },
            {
                "category": "Multichannel Coordination",
                "question": "What feature helps prevent users from receiving too many messages across channels?",
                "options": {
                    "A": "Frequency Capping",
                    "B": "Message Throttling",
                    "C": "Communication Limits",
                    "D": "Channel Restrictions"
                },
                "correct": "A"
            },
            {
                "category": "Multichannel Coordination",
                "question": "How can you ensure consistent messaging across email, push, and in-app channels?",
                "options": {
                    "A": "By using the same content for all channels",
                    "B": "By using Content Blocks to maintain shared elements",
                    "C": "By limiting campaigns to one channel at a time",
                    "D": "By creating separate teams for each channel"
                },
                "correct": "B"
            },
            {
                "category": "Multichannel Coordination",
                "question": "What is Channel Coordination in Braze Canvas?",
                "options": {
                    "A": "Setting up SMS fallbacks for email",
                    "B": "Configuring which departments can use which channels",
                    "C": "Orchestrating customer journeys across multiple messaging channels",
                    "D": "Adjusting send times to business hours"
                },
                "correct": "C"
            },
            {
                "category": "Data Management",
                "question": "What is the purpose of the 'Identity Resolution' feature in Braze?",
                "options": {
                    "A": "Verifying user identities through two-factor authentication",
                    "B": "Merging user profiles that belong to the same person",
                    "C": "Resolving conflicting data from different sources",
                    "D": "Anonymizing user data for privacy"
                },
                "correct": "B"
            },
            {
                "category": "Data Management",
                "question": "How long does Braze retain user profile data by default?",
                "options": {
                    "A": "30 days",
                    "B": "6 months",
                    "C": "1 year",
                    "D": "Indefinitely, until explicitly deleted"
                },
                "correct": "D"
            },
            {
                "category": "Data Management",
                "question": "What happens to custom event data in Braze?",
                "options": {
                    "A": "It's stored for 90 days",
                    "B": "It's summarized after 24 hours",
                    "C": "It's permanently stored in raw form",
                    "D": "It's encrypted and cannot be modified"
                },
                "correct": "A"
            },
            {
                "category": "Privacy and Compliance",
                "question": "Which of the following is a key GDPR capability in Braze?",
                "options": {
                    "A": "Automatic content moderation",
                    "B": "User data export and deletion capabilities",
                    "C": "Legal document templates",
                    "D": "Government reporting tools"
                },
                "correct": "B"
            },
            {
                "category": "Privacy and Compliance",
                "question": "How does Braze help with email compliance?",
                "options": {
                    "A": "By automatically scanning content for compliance issues",
                    "B": "By providing legal consultation",
                    "C": "By including mandatory unsubscribe links and managing subscription preferences",
                    "D": "By limiting email frequency"
                },
                "correct": "C"
            }
        ]
    
    def _create_question_set_three(self):
        
        return [
            {
                "category": "Technical Implementation",
                "question": "What REST API endpoint would you use to track user events?",
                "options": {
                    "A": "/users/identify",
                    "B": "/users/track",
                    "C": "/events/track",
                    "D": "/users/events"
                },
                "correct": "B"
            },
            {
                "category": "Technical Implementation",
                "question": "Which method must be called before logging events in the Braze SDK?",
                "options": {
                    "A": "openSession()",
                    "B": "initBraze()",
                    "C": "changeUser()",
                    "D": "startTracking()"
                },
                "correct": "C"
            },
            {
                "category": "Technical Implementation",
                "question": "What is the correct way to identify a user via the Braze REST API?",
                "options": {
                    "A": "POST /users/identify with external_id",
                    "B": "POST /users/track with external_id",
                    "C": "POST /users/identify with user_aliases",
                    "D": "POST /users/alias with external_id"
                },
                "correct": "A"
            },
            {
                "category": "Technical Implementation",
                "question": "What is the best practice for handling anonymous users in the Braze SDK?",
                "options": {
                    "A": "Do not track any data until a user is identified",
                    "B": "Create a temporary ID using the device ID",
                    "C": "Use an anonymous ID that can later be merged with an identified user",
                    "D": "Send all data without an ID"
                },
                "correct": "C"
            },
            {
                "category": "Technical Implementation",
                "question": "What is the maximum size of a custom attribute value in Braze?",
                "options": {
                    "A": "256 bytes",
                    "B": "5 KB",
                    "C": "50 KB",
                    "D": "No limit"
                },
                "correct": "C"
            },
            {
                "category": "SDK Integration",
                "question": "Which of the following is NOT a supported Braze SDK platform?",
                "options": {
                    "A": "iOS",
                    "B": "Android",
                    "C": "Windows Phone",
                    "D": "Web"
                },
                "correct": "C"
            },
            {
                "category": "SDK Integration",
                "question": "How should you handle push notification tokens in the Braze SDK?",
                "options": {
                    "A": "Manually register them via the API",
                    "B": "Let the SDK automatically register them",
                    "C": "Store them in a custom attribute",
                    "D": "Pass them to your server first"
                },
                "correct": "B"
            },
            {
                "category": "SDK Integration",
                "question": "What is the purpose of the 'appboy.min.js' file in a web implementation?",
                "options": {
                    "A": "To load custom styling",
                    "B": "To handle user tracking and messaging",
                    "C": "To create a data backup",
                    "D": "To manage user permissions"
                },
                "correct": "B"
            },
            {
                "category": "SDK Integration",
                "question": "What does the Braze SDK 'requestImmediateDataFlush()' method do?",
                "options": {
                    "A": "Clears local data storage",
                    "B": "Immediately sends queued data to Braze servers",
                    "C": "Updates all user attributes",
                    "D": "Refreshes content from the server"
                },
                "correct": "B"
            },
            {
                "category": "API Usage",
                "question": "What authentication method does the Braze API use?",
                "options": {
                    "A": "OAuth 2.0",
                    "B": "API Keys in request headers",
                    "C": "Username and password",
                    "D": "JWT tokens"
                },
                "correct": "B"
            },
            {
                "category": "API Usage",
                "question": "What is the rate limit policy for the Braze API?",
                "options": {
                    "A": "Fixed at 100 requests per minute",
                    "B": "Fixed at 250,000 requests per day",
                    "C": "Varies by endpoint and plan",
                    "D": "No rate limits"
                },
                "correct": "C"
            },
            {
                "category": "API Usage",
                "question": "Which endpoint would you use to send a transactional message to a specific user?",
                "options": {
                    "A": "/campaigns/trigger/send",
                    "B": "/messages/send",
                    "C": "/users/message",
                    "D": "/transactional/send"
                },
                "correct": "A"
            },
            {
                "category": "API Usage",
                "question": "What is the correct format for sending arrays of user attributes via the API?",
                "options": {
                    "A": "As comma-separated strings",
                    "B": "As JSON arrays",
                    "C": "As multiple separate fields",
                    "D": "As serialized binary data"
                },
                "correct": "B"
            },
            {
                "category": "Webhooks",
                "question": "What is the primary use case for Braze Webhooks?",
                "options": {
                    "A": "To track website visitors",
                    "B": "To send data to external systems when users take specific actions",
                    "C": "To accept inbound messages",
                    "D": "To monitor system performance"
                },
                "correct": "B"
            },
            {
                "category": "Webhooks",
                "question": "What HTTP methods can Braze Webhooks use?",
                "options": {
                    "A": "Only GET",
                    "B": "Only POST",
                    "C": "GET, POST, PUT, or DELETE",
                    "D": "Only PUT"
                },
                "correct": "C"
            },
            {
                "category": "Webhooks",
                "question": "How can you include user-specific data in a webhook payload?",
                "options": {
                    "A": "By including user IDs in the query string",
                    "B": "By using Liquid personalization in the request body",
                    "C": "It's not possible to personalize webhooks",
                    "D": "By creating a separate webhook for each user"
                },
                "correct": "B"
            },
            {
                "category": "Data Schema",
                "question": "What is the best practice for naming custom events in Braze?",
                "options": {
                    "A": "Use all lowercase with underscores",
                    "B": "Use camelCase",
                    "C": "Use PascalCase",
                    "D": "Use spaces between words"
                },
                "correct": "A"
            },
            {
                "category": "Data Schema",
                "question": "What happens if you exceed the limit of 250 custom attributes per app?",
                "options": {
                    "A": "The app will crash",
                    "B": "New attributes will overwrite old ones",
                    "C": "New attributes will be ignored",
                    "D": "You'll be charged an overage fee"
                },
                "correct": "C"
            },
            {
                "category": "Data Schema",
                "question": "What data type should be used for storing date values as custom attributes?",
                "options": {
                    "A": "String in ISO 8601 format",
                    "B": "Unix timestamp as an integer",
                    "C": "Date object",
                    "D": "String in MM/DD/YYYY format"
                },
                "correct": "C"
            },
            {
                "category": "Advanced SDK Features",
                "question": "What is the purpose of the Braze SDK's 'SdkAuthenticationDelegate'?",
                "options": {
                    "A": "To authenticate users to your app",
                    "B": "To verify the Braze API key",
                    "C": "To enable secure authentication of the SDK to Braze servers",
                    "D": "To manage user login sessions"
                },
                "correct": "C"
            },
            {
                "category": "Advanced SDK Features",
                "question": "How can you implement location tracking with the Braze SDK?",
                "options": {
                    "A": "It happens automatically",
                    "B": "By calling the logLocation() method with coordinates",
                    "C": "By connecting to Google Maps API",
                    "D": "By enabling geofences"
                },
                "correct": "B"
            },
            {
                "category": "Advanced SDK Features",
                "question": "What is the 'dev_options' parameter used for in the Braze Web SDK?",
                "options": {
                    "A": "To enable console logging for debugging",
                    "B": "To restrict usage to development environments",
                    "C": "To access beta features",
                    "D": "To modify API endpoints"
                },
                "correct": "A"
            },
            {
                "category": "In-App Message Customization",
                "question": "How can you display a custom view for in-app messages?",
                "options": {
                    "A": "By modifying the HTML/CSS directly in the dashboard",
                    "B": "By implementing a custom message delegate in the SDK",
                    "C": "By creating a custom webhook",
                    "D": "It's not possible to customize in-app message display"
                },
                "correct": "B"
            },
            {
                "category": "In-App Message Customization",
                "question": "What is required to implement a custom HTML in-app message?",
                "options": {
                    "A": "External web hosting",
                    "B": "Only CSS customization",
                    "C": "JavaScript knowledge for interaction handling",
                    "D": "Server-side rendering"
                },
                "correct": "C"
            },
            {
                "category": "In-App Message Customization",
                "question": "How can in-app messages be triggered programmatically?",
                "options": {
                    "A": "By calling displayNextInAppMessage()",
                    "B": "By manually creating an Action-Based Campaign",
                    "C": "By sending a push notification first",
                    "D": "It's not possible to trigger them programmatically"
                },
                "correct": "A"
            },
            {
                "category": "Push Notifications",
                "question": "What is required to implement push notifications on iOS?",
                "options": {
                    "A": "APNs certificate or key",
                    "B": "Google Cloud Messaging key",
                    "C": "SMS gateway credentials",
                    "D": "Email server configuration"
                },
                "correct": "A"
            },
            {
                "category": "Push Notifications",
                "question": "How does Braze handle push notification deep linking?",
                "options": {
                    "A": "Through a dedicated API endpoint",
                    "B": "Through URI schemes or universal links defined in the notification payload",
                    "C": "It doesn't support deep linking",
                    "D": "Through QR codes"
                },
                "correct": "B"
            },
            {
                "category": "Push Notifications",
                "question": "What is the maximum size of a push notification payload on iOS?",
                "options": {
                    "A": "2KB",
                    "B": "4KB",
                    "C": "10KB",
                    "D": "Unlimited"
                },
                "correct": "B"
            },
            {
                "category": "Data Integration",
                "question": "Which of these is NOT a supported integration partner for Braze?",
                "options": {
                    "A": "Segment",
                    "B": "mParticle",
                    "C": "Zapier",
                    "D": "Oracle Database"
                },
                "correct": "D"
            },
            {
                "category": "Data Integration",
                "question": "What is Currents in Braze used for?",
                "options": {
                    "A": "Real-time data exports to external systems",
                    "B": "Measuring electrical usage of servers",
                    "C": "Tracking currency conversions",
                    "D": "Managing server load"
                },
                "correct": "A"
            }
        ]



    def get_question_set(self, index):
        """Return the specified question set (0, 1, 2, 3, 4)"""
        return self._question_sets[index % 5]
        
    def get_set_names(self):
        """Return names for the question sets"""
        return ["Practitioner Learning Path", "Developer Learning Path","Basic Braze Knowledge", "Advanced Features", "Technical Implementation" ]
        
    def get_total_sets(self):
        """Return the total number of question sets available"""
        return len(self._question_sets)