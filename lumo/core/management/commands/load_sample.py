# core/management/commands/load_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from services.models import Service
from portfolio.models import Project
from blog.models import Post
from datetime import datetime

class Command(BaseCommand):
    help = 'Load sample data for Lumo Software Solutions'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create superuser if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@lumosoft.co.za',
                password='admin123'
            )
            self.stdout.write('Created admin user (username: admin, password: admin123)')
        
        # Load Services
        # services/models.py - Sample data for Service model
        services_data = [
            {
                'title': 'Custom Software Development',
                'slug': 'custom-software-development',
                'short_description': 'Tailored software solutions designed to address your specific business challenges.',
                'detailed_description': 'We build bespoke software applications that streamline your operations, automate processes, and solve unique business problems. Our solutions are scalable, maintainable, and designed to grow with your business.',
                'icon_class': 'fas fa-code',
                'sort_order': 1
            },
            {
                'title': 'Web Application Development',
                'slug': 'web-application-development',
                'short_description': 'Responsive, high-performance web applications that deliver exceptional user experiences.',
                'detailed_description': 'From single-page applications to complex enterprise systems, we create web solutions that are fast, secure, and user-friendly using modern frameworks and best practices.',
                'icon_class': 'fas fa-globe',
                'sort_order': 2
            },
            {
                'title': 'Mobile App Development',
                'slug': 'mobile-app-development',
                'short_description': 'Native and cross-platform mobile applications for iOS and Android platforms.',
                'detailed_description': 'We develop mobile apps that provide seamless user experiences across all devices. Whether you need native iOS/Android apps or cross-platform solutions, we have the expertise to deliver.',
                'icon_class': 'fas fa-mobile-alt',
                'sort_order': 3
            },
            {
                'title': 'Cloud Solutions & DevOps',
                'slug': 'cloud-solutions-devops',
                'short_description': 'Scalable cloud infrastructure and deployment automation services.',
                'detailed_description': 'We help businesses migrate to the cloud, optimize their infrastructure, and implement DevOps practices for continuous integration and deployment.',
                'icon_class': 'fas fa-cloud',
                'sort_order': 4
            },
            {
                'title': 'Data Analytics & BI',
                'slug': 'data-analytics-bi',
                'short_description': 'Transform your data into actionable insights with advanced analytics.',
                'detailed_description': 'Our data analytics solutions help you make informed decisions by turning raw data into meaningful visualizations and reports.',
                'icon_class': 'fas fa-chart-line',
                'sort_order': 5
            },
            {
                'title': 'E-commerce Solutions',
                'slug': 'ecommerce-solutions',
                'short_description': 'Complete online store development with advanced features and integrations.',
                'detailed_description': 'We build robust e-commerce platforms with secure payment processing, inventory management, and seamless customer experiences.',
                'icon_class': 'fas fa-shopping-cart',
                'sort_order': 6
            }
        ]
                
        for service_data in services_data:
            Service.objects.get_or_create(
                slug=service_data['slug'],
                defaults=service_data
            )
        
        self.stdout.write(f'Loaded {len(services_data)} services')
        
        # Load Projects
        # portfolio/models.py - Sample data for Project model
        projects_data = [
            {
                'title': 'MediCare Patient Management System',
                'slug': 'medicare-patient-management-system',
                'client': 'MediCare Health Group',
                'description': 'A comprehensive patient management system for healthcare facilities with appointment scheduling, electronic health records, and billing integration.',
                'full_case_study': 'Developed a full-stack healthcare management solution that reduced patient wait times by 40% and improved record accuracy. The system integrates with existing hospital infrastructure and complies with healthcare regulations.',
                'category': 'WEB',
                'technologies_used': 'Django, React, PostgreSQL, Docker, AWS',
                'is_featured': True,
                'completion_date': '2023-08-15',
                'website_url': 'https://medicare-demo.lumosoft.co.za',
                'github_url': ''
            },
            {
                'title': 'FinTrack Investment Dashboard',
                'slug': 'fintrack-investment-dashboard',
                'client': 'WealthFront Capital',
                'description': 'Real-time investment tracking dashboard with portfolio analytics and market insights.',
                'full_case_study': 'Built a financial analytics platform that processes real-time market data and provides personalized investment insights. The dashboard helped clients increase portfolio returns by 15% through better decision-making.',
                'category': 'SOFT',
                'technologies_used': 'Python, FastAPI, Vue.js, MongoDB, Redis',
                'is_featured': True,
                'completion_date': '2023-05-22',
                'website_url': 'https://fintrack-demo.lumosoft.co.za',
                'github_url': ''
            },
            {
                'title': 'EduLearn LMS Platform',
                'slug': 'edulearn-lms-platform',
                'client': 'Digital Learning Institute',
                'description': 'Interactive learning management system for online education with video streaming and assessment tools.',
                'full_case_study': 'Created a scalable e-learning platform supporting 10,000+ concurrent users. Features include video conferencing, automated grading, and interactive course materials that increased student engagement by 60%.',
                'category': 'WEB',
                'technologies_used': 'Django, React, WebRTC, PostgreSQL, Azure',
                'is_featured': True,
                'completion_date': '2023-02-10',
                'website_url': 'https://edulearn-demo.lumosoft.co.za',
                'github_url': ''
            },
            {
                'title': 'SmartHome IoT Automation',
                'slug': 'smarthome-iot-automation',
                'client': 'HomeTech Solutions',
                'description': 'IoT-based home automation system with mobile control and energy monitoring.',
                'full_case_study': 'Developed a comprehensive smart home solution integrating various IoT devices. The system reduces energy consumption by 25% through intelligent automation and provides seamless control via mobile app.',
                'category': 'SOFT',
                'technologies_used': 'Python, Raspberry Pi, MQTT, React Native, AWS IoT',
                'is_featured': True,
                'completion_date': '2022-11-30',
                'website_url': '',
                'github_url': 'https://github.com/lumosoft/smarthome-iot'
            },
            {
                'title': 'RetailPro Inventory System',
                'slug': 'retailpro-inventory-system',
                'client': 'Urban Retail Chain',
                'description': 'Advanced inventory management system with predictive analytics and supplier integration.',
                'full_case_study': 'Built an inventory optimization system that reduced stockouts by 70% and improved inventory turnover. The system uses machine learning to predict demand and automate reordering.',
                'category': 'SOFT',
                'technologies_used': 'Django, React, TensorFlow, PostgreSQL, Docker',
                'is_featured': False,
                'completion_date': '2023-01-15',
                'website_url': 'https://retailpro-demo.lumosoft.co.za',
                'github_url': ''
            },
            {
                'title': 'ConnectCRM Sales Platform',
                'slug': 'connectcrm-sales-platform',
                'client': 'SalesForce Partners',
                'description': 'Customer relationship management platform with sales automation and analytics.',
                'full_case_study': 'Developed a custom CRM that increased sales team productivity by 35% through automation and better lead management. The platform integrates with email, calendar, and marketing tools.',
                'category': 'WEB',
                'technologies_used': 'Django, Vue.js, Celery, PostgreSQL, Redis',
                'is_featured': True,
                'completion_date': '2022-09-20',
                'website_url': 'https://connectcrm-demo.lumosoft.co.za',
                'github_url': ''
            },
            {
                'title': 'FoodExpress Delivery App',
                'slug': 'foodexpress-delivery-app',
                'client': 'QuickBite Restaurants',
                'description': 'Food delivery mobile application with real-time tracking and payment processing.',
                'full_case_study': 'Created a food delivery platform serving 50+ restaurants. The app features real-time order tracking, multiple payment options, and a sophisticated delivery routing algorithm.',
                'category': 'SOFT',
                'technologies_used': 'React Native, Node.js, MongoDB, Firebase, Stripe API',
                'is_featured': False,
                'completion_date': '2023-03-08',
                'website_url': '',
                'github_url': ''
            },
            {
                'title': 'Cloud Migration Strategy',
                'slug': 'cloud-migration-strategy',
                'client': 'Enterprise Solutions Inc.',
                'description': 'Comprehensive cloud migration plan and implementation for legacy systems.',
                'full_case_study': 'Provided consulting and implementation services for migrating legacy systems to AWS. Reduced infrastructure costs by 40% while improving scalability and reliability.',
                'category': 'CONS',
                'technologies_used': 'AWS, Docker, Kubernetes, Terraform, Python',
                'is_featured': True,
                'completion_date': '2022-12-05',
                'website_url': '',
                'github_url': ''
            }
        ]
                
        for project_data in projects_data:
            # Convert string date to date object
            project_data['completion_date'] = datetime.strptime(
                project_data['completion_date'], '%Y-%m-%d'
            ).date()
            
            Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
        
        self.stdout.write(f'Loaded {len(projects_data)} projects')
        
        # Load Blog Posts
        # blog/models.py - Sample data for Post model
        blog_posts_data = [
            {
                'title': 'The Future of Web Development: Trends to Watch in 2024',
                'slug': 'future-web-development-trends-2024',
                'excerpt': 'Explore the emerging technologies and methodologies that are shaping the future of web development.',
                'content': '''
                <h2>Introduction</h2>
                <p>Web development continues to evolve at a rapid pace, with new frameworks, tools, and methodologies emerging regularly. As we look toward 2024, several key trends are poised to shape the landscape of web development.</p>
                
                <h2>1. AI-Powered Development</h2>
                <p>Artificial intelligence is revolutionizing how we build websites and applications. From code generation to automated testing, AI tools are becoming increasingly sophisticated.</p>
                
                <h2>2. Serverless Architecture</h2>
                <p>Serverless computing continues to gain traction, offering scalability and cost-efficiency for applications of all sizes.</p>
                
                <h2>3. WebAssembly (WASM)</h2>
                <p>WebAssembly enables high-performance applications to run in the browser, opening up new possibilities for web applications.</p>
                
                <h2>Conclusion</h2>
                <p>Staying ahead of these trends will be crucial for developers and businesses looking to maintain competitive advantage in the digital landscape.</p>
                ''',
                'published': True,
                'published_date': '2023-10-15 09:00:00'
            },
            {
                'title': 'Why Django is Still the Best Choice for Enterprise Applications',
                'slug': 'django-enterprise-applications-choice',
                'excerpt': 'Discover why Django remains a top choice for building robust, scalable enterprise applications.',
                'content': '''
                <h2>The Django Advantage</h2>
                <p>Django has been a reliable framework for web development for over a decade, and its popularity continues to grow, especially in enterprise environments.</p>
                
                <h2>Security Features</h2>
                <p>Django provides built-in protection against common security threats like SQL injection, cross-site scripting, and CSRF attacks.</p>
                
                <h2>Scalability</h2>
                <p>With proper architecture, Django applications can handle millions of users and massive amounts of data.</p>
                
                <h2>Batteries-Included Philosophy</h2>
                <p>Django comes with everything you need to build complete web applications, reducing development time and complexity.</p>
                
                <h2>Real-World Success Stories</h2>
                <p>Companies like Instagram, Pinterest, and NASA continue to rely on Django for their critical applications.</p>
                ''',
                'published': True,
                'published_date': '2023-09-22 14:30:00'
            },
            {
                'title': 'Mobile-First Development: Strategies for Success',
                'slug': 'mobile-first-development-strategies',
                'excerpt': 'Learn effective strategies for implementing mobile-first design and development in your projects.',
                'content': '''
                <h2>Understanding Mobile-First</h2>
                <p>Mobile-first development means designing for mobile devices first, then scaling up to larger screens, rather than the traditional desktop-first approach.</p>
                
                <h2>Benefits of Mobile-First</h2>
                <ul>
                    <li>Improved performance on mobile devices</li>
                    <li>Better user experience across all devices</li>
                    <li>Higher search engine rankings</li>
                    <li>Future-proof design approach</li>
                </ul>
                
                <h2>Implementation Strategies</h2>
                <p>Start with a minimal viable product for mobile, then progressively enhance for larger screens using CSS media queries.</p>
                
                <h2>Tools and Frameworks</h2>
                <p>Modern CSS frameworks like Bootstrap and Tailwind CSS make mobile-first development more accessible than ever.</p>
                ''',
                'published': True,
                'published_date': '2023-08-30 11:15:00'
            },
            {
                'title': 'The Role of DevOps in Modern Software Development',
                'slug': 'devops-modern-software-development',
                'excerpt': 'How DevOps practices are transforming software development and deployment processes.',
                'content': '''
                <h2>What is DevOps?</h2>
                <p>DevOps is a set of practices that combines software development and IT operations to shorten the systems development life cycle.</p>
                
                <h2>Key Benefits</h2>
                <ul>
                    <li>Faster time to market</li>
                    <li>Improved deployment frequency</li>
                    <li>More stable operating environments</li>
                    <li>Better communication and collaboration</li>
                </ul>
                
                <h2>Essential DevOps Tools</h2>
                <p>From Docker and Kubernetes to Jenkins and GitLab CI, the DevOps toolchain continues to evolve and improve.</p>
                
                <h2>Getting Started with DevOps</h2>
                <p>Begin with continuous integration and gradually implement more advanced practices like infrastructure as code and monitoring.</p>
                ''',
                'published': True,
                'published_date': '2023-07-18 16:45:00'
            }
        ]
        
        admin_user = User.objects.get(username='admin')
        
        for post_data in blog_posts_data:
            # Convert string datetime to datetime object
            post_data['published_date'] = datetime.strptime(
                post_data['published_date'], '%Y-%m-%d %H:%M:%S'
            )
            post_data['author'] = admin_user
            
            Post.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
        
        self.stdout.write(f'Loaded {len(blog_posts_data)} blog posts')
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded all sample data!')
        )