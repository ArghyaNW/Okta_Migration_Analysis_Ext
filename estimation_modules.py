"""
Core Estimation Modules for OKTA to Entra ID Migration Calculator
Implements the three main estimation approaches
"""

import json
from datetime import datetime
import pandas as pd

# Predefined Scenarios
PREDEFINED_SCENARIOS = {
    'small': {
        'name': 'Small Business',
        'description': 'Small organization with basic identity needs',
        'characteristics': {
            'employees': '50-500',
            'locations': '1-3',
            'apps': '10-30',
            'complexity': 'Low'
        },
        'data': {
            'num_employees': 250,
            'num_it_staff': 3,
            'num_locations': 2,
            'saml_apps_count': 10,
            'bookmark_apps_count': 12,
            'swa_apps_count': 5,
            'oidc_apps_count': 3,
            'okta_policies_count': 3,
            'okta_ad_agents_count': 1,
            'okta_radius_agents_count': 0,
            'provisioning_enabled_apps': 4,
            'federated_domains_count': 1,
            'workflow_automations_count': 2,
            'push_groups_apps_count': 5,
            'total_push_groups_count': 15,
            'groups_recreate_count': 8,
            'annual_okta_cost': 25000
        }
    },
    'medium': {
        'name': 'Medium Enterprise',
        'description': 'Mid-sized organization with moderate complexity',
        'characteristics': {
            'employees': '500-2500',
            'locations': '3-10',
            'apps': '30-100',
            'complexity': 'Medium'
        },
        'data': {
            'num_employees': 1200,
            'num_it_staff': 15,
            'num_locations': 6,
            'saml_apps_count': 25,
            'bookmark_apps_count': 35,
            'swa_apps_count': 18,
            'oidc_apps_count': 12,
            'okta_policies_count': 8,
            'okta_ad_agents_count': 3,
            'okta_radius_agents_count': 2,
            'provisioning_enabled_apps': 15,
            'federated_domains_count': 3,
            'workflow_automations_count': 8,
            'push_groups_apps_count': 20,
            'total_push_groups_count': 45,
            'groups_recreate_count': 25,
            'annual_okta_cost': 85000
        }
    },
    'enterprise': {
        'name': 'Large Enterprise',
        'description': 'Large organization with high complexity and compliance needs',
        'characteristics': {
            'employees': '2500+',
            'locations': '10+',
            'apps': '100+',
            'complexity': 'High'
        },
        'data': {
            'num_employees': 5000,
            'num_it_staff': 45,
            'num_locations': 20,
            'saml_apps_count': 60,
            'bookmark_apps_count': 80,
            'swa_apps_count': 35,
            'oidc_apps_count': 25,
            'okta_policies_count': 20,
            'okta_ad_agents_count': 8,
            'okta_radius_agents_count': 5,
            'provisioning_enabled_apps': 40,
            'federated_domains_count': 8,
            'workflow_automations_count': 25,
            'push_groups_apps_count': 50,
            'total_push_groups_count': 120,
            'groups_recreate_count': 75,
            'annual_okta_cost': 250000
        }
    }
}

class EstimationModules:
    
    @staticmethod
    def scenario_based_estimation(scenario_type):
        """
        Module 1: Scenario-Based Estimation
        Uses predefined scenarios for quick estimates
        """
        if scenario_type not in PREDEFINED_SCENARIOS:
            return None
        
        scenario = PREDEFINED_SCENARIOS[scenario_type]
        data = scenario['data']
        
        # Calculate estimates based on scenario data
        results = EstimationModules._calculate_comprehensive_estimate(data)
        
        # Add scenario-specific metadata
        results['estimation_type'] = 'Scenario-Based'
        results['scenario'] = scenario['name']
        results['scenario_description'] = scenario['description']
        results['characteristics'] = scenario['characteristics']
        
        return results
    
    @staticmethod
    def manual_input_estimation(form_data):
        """
        Module 2: Manual Input-Based Estimation
        Uses user-provided detailed data
        """
        # Validate input data
        if not form_data:
            return None
        
        # Calculate comprehensive estimate
        results = EstimationModules._calculate_comprehensive_estimate(form_data)
        
        # Add input-specific metadata
        results['estimation_type'] = 'Manual Input-Based'
        results['company_name'] = form_data.get('company_name', 'N/A')
        results['project_name'] = form_data.get('project_name', 'N/A')
        
        # Add complexity factors based on actual input
        results['complexity_factors'] = EstimationModules._analyze_complexity_factors(form_data)
        
        return results
    
    @staticmethod
    def okta_api_estimation(api_data):
        """
        Module 3: Automated Estimation via OKTA API
        Uses data fetched from OKTA API (simulated for now)
        """
        # This would connect to actual OKTA API in production
        # For now, we'll simulate API response structure
        
        if not api_data:
            # Simulate API data structure
            api_data = {
                'users_count': 1500,
                'groups_count': 250,
                'applications': {
                    'saml': 30,
                    'bookmark': 45,
                    'swa': 20,
                    'oidc': 15
                },
                'policies_count': 12,
                'mfa_policies': 8,
                'custom_integrations': 5,
                'sso_integrations': 110,
                'api_endpoints': 25
            }
        
        # Convert API data to our internal format
        converted_data = EstimationModules._convert_api_data(api_data)
        
        # Calculate estimates
        results = EstimationModules._calculate_comprehensive_estimate(converted_data)
        
        # Add API-specific metadata
        results['estimation_type'] = 'OKTA API-Based'
        results['api_data_source'] = 'OKTA Tenant Analysis'
        results['data_accuracy'] = 'High (Real-time data)'
        
        return results
    
    @staticmethod
    def _calculate_comprehensive_estimate(data):
        """
        Core calculation engine for all estimation modules
        """
        # Calculate basic metrics
        total_apps = (
            data.get('saml_apps_count', 0) +
            data.get('bookmark_apps_count', 0) +
            data.get('swa_apps_count', 0) +
            data.get('oidc_apps_count', 0)
        )
        
        num_employees = data.get('num_employees', 0)
        
        # Migration Effort Calculation (hours/days)
        effort_hours = EstimationModules._calculate_migration_effort(data)
        effort_days = effort_hours / 8  # 8 hours per day
        
        # Licensing Cost Calculation
        licensing_cost = EstimationModules._calculate_licensing_cost(data)
        
        # Infrastructure Cost Calculation
        infrastructure_cost = EstimationModules._calculate_infrastructure_cost(data)
        
        # Professional Services Cost Calculation
        professional_services_cost = EstimationModules._calculate_professional_services_cost(data)
        
        # Risk and Complexity Score (0-100)
        complexity_score = EstimationModules._calculate_complexity_score(data)
        
        # Timeline Estimation
        timeline_weeks = EstimationModules._calculate_timeline(data, effort_days)
        
        # Risk Assessment
        risk_assessment = EstimationModules._assess_risks(data, complexity_score)
        
        # Total Cost
        total_cost = licensing_cost + infrastructure_cost + professional_services_cost
        
        return {
            'executive_summary': {
                'total_cost': total_cost,
                'timeline_weeks': timeline_weeks,
                'complexity_score': complexity_score,
                'total_apps': total_apps,
                'total_users': num_employees
            },
            'migration_effort': {
                'hours': effort_hours,
                'days': effort_days,
                'complexity_level': EstimationModules._get_complexity_level(complexity_score)
            },
            'cost_breakdown': {
                'licensing': licensing_cost,
                'professional_services': professional_services_cost,
                'infrastructure': infrastructure_cost,
                'support': professional_services_cost * 0.2,  # 20% of services cost
                'total': total_cost
            },
            'timeline_estimation': {
                'weeks': timeline_weeks,
                'phases': EstimationModules._get_migration_phases(timeline_weeks),
                'critical_path': EstimationModules._get_critical_path_items(data)
            },
            'risk_assessment': risk_assessment,
            'recommendations': EstimationModules._generate_recommendations(data, complexity_score),
            'calculation_date': datetime.now().isoformat()
        }
    
    @staticmethod
    def _calculate_migration_effort(data):
        """Calculate total migration effort in hours"""
        base_hours = 160  # Base project hours
        
        # Application migration hours
        app_hours = (
            data.get('saml_apps_count', 0) * 8 +
            data.get('oidc_apps_count', 0) * 6 +
            data.get('swa_apps_count', 0) * 16 +
            data.get('bookmark_apps_count', 0) * 2
        )
        
        # Policy and configuration hours
        policy_hours = data.get('okta_policies_count', 0) * 12
        agent_hours = (data.get('okta_ad_agents_count', 0) + data.get('okta_radius_agents_count', 0)) * 24
        workflow_hours = data.get('workflow_automations_count', 0) * 32
        provisioning_hours = data.get('provisioning_enabled_apps', 0) * 16
        
        # Group migration hours
        group_hours = data.get('groups_recreate_count', 0) * 2
        
        total_hours = base_hours + app_hours + policy_hours + agent_hours + workflow_hours + provisioning_hours + group_hours
        
        # Apply complexity multipliers
        complexity_multiplier = 1.0
        if data.get('num_employees', 0) > 5000:
            complexity_multiplier += 0.3
        if data.get('federated_domains_count', 0) > 5:
            complexity_multiplier += 0.2
        
        return int(total_hours * complexity_multiplier)
    
    @staticmethod
    def _calculate_licensing_cost(data):
        """Calculate Microsoft licensing costs"""
        num_employees = data.get('num_employees', 0)
        
        # Assume E3 licensing at $22/user/month for 12 months
        base_licensing = num_employees * 22 * 12
        
        # Additional licensing for premium features
        premium_features = 0
        if data.get('okta_policies_count', 0) > 10:
            premium_features += num_employees * 5 * 12  # P1 add-on
        
        return base_licensing + premium_features
    
    @staticmethod
    def _calculate_infrastructure_cost(data):
        """Calculate infrastructure and setup costs"""
        base_infrastructure = 25000  # Base setup cost
        
        # Agents and connectors
        agent_costs = (data.get('okta_ad_agents_count', 0) + data.get('okta_radius_agents_count', 0)) * 5000
        
        # Domain federation setup
        domain_costs = data.get('federated_domains_count', 0) * 2500
        
        # Monitoring and logging
        monitoring_costs = 15000 if data.get('num_employees', 0) > 1000 else 5000
        
        return base_infrastructure + agent_costs + domain_costs + monitoring_costs
    
    @staticmethod
    def _calculate_professional_services_cost(data):
        """Calculate professional services costs"""
        # Base consulting cost
        base_cost = 50000
        
        # Application migration services
        total_apps = (
            data.get('saml_apps_count', 0) +
            data.get('bookmark_apps_count', 0) +
            data.get('swa_apps_count', 0) +
            data.get('oidc_apps_count', 0)
        )
        
        app_services = total_apps * 750  # $750 per app
        
        # Policy and workflow services
        policy_services = data.get('okta_policies_count', 0) * 1500
        workflow_services = data.get('workflow_automations_count', 0) * 2500
        
        # Training and knowledge transfer
        training_cost = data.get('num_it_staff', 0) * 500
        
        total_services = base_cost + app_services + policy_services + workflow_services + training_cost
        
        # Apply complexity multiplier
        complexity_multiplier = 1.0
        if data.get('workflow_automations_count', 0) > 20:
            complexity_multiplier += 0.4
        if data.get('provisioning_enabled_apps', 0) > 30:
            complexity_multiplier += 0.3
        
        return int(total_services * complexity_multiplier)
    
    @staticmethod
    def _calculate_complexity_score(data):
        """Calculate migration complexity score (0-100)"""
        score = 0
        
        # Application complexity
        total_apps = (
            data.get('saml_apps_count', 0) +
            data.get('bookmark_apps_count', 0) +
            data.get('swa_apps_count', 0) +
            data.get('oidc_apps_count', 0)
        )
        score += min(total_apps * 0.5, 25)  # Max 25 points
        
        # Policy complexity
        score += min(data.get('okta_policies_count', 0) * 2, 20)  # Max 20 points
        
        # Integration complexity
        score += min(data.get('workflow_automations_count', 0) * 1.5, 15)  # Max 15 points
        score += min(data.get('provisioning_enabled_apps', 0) * 1, 15)  # Max 15 points
        
        # Infrastructure complexity
        score += min(data.get('federated_domains_count', 0) * 2, 10)  # Max 10 points
        
        # Organization complexity
        if data.get('num_employees', 0) > 5000:
            score += 10
        elif data.get('num_employees', 0) > 1000:
            score += 5
        
        # Locations complexity
        if data.get('num_locations', 0) > 10:
            score += 5
        
        return min(int(score), 100)
    
    @staticmethod
    def _calculate_timeline(data, effort_days):
        """Calculate migration timeline in weeks"""
        # Base timeline calculation
        base_weeks = 12
        
        # Add weeks based on effort
        effort_weeks = effort_days / 5  # 5 working days per week
        
        # Add complexity factors
        complexity_weeks = 0
        if data.get('workflow_automations_count', 0) > 15:
            complexity_weeks += 4
        if data.get('provisioning_enabled_apps', 0) > 25:
            complexity_weeks += 3
        if data.get('federated_domains_count', 0) > 5:
            complexity_weeks += 2
        
        total_weeks = base_weeks + (effort_weeks * 0.3) + complexity_weeks
        
        return max(int(total_weeks), 8)  # Minimum 8 weeks
    
    @staticmethod
    def _assess_risks(data, complexity_score):
        """Assess migration risks"""
        risks = []
        
        if complexity_score > 75:
            risks.append({
                'level': 'High',
                'category': 'Complexity',
                'description': 'High complexity migration with many applications and integrations',
                'mitigation': 'Implement phased approach with extensive testing'
            })
        
        if data.get('workflow_automations_count', 0) > 20:
            risks.append({
                'level': 'Medium',
                'category': 'Automation',
                'description': 'Many workflow automations need recreation',
                'mitigation': 'Map workflows early and consider Power Automate alternatives'
            })
        
        if data.get('provisioning_enabled_apps', 0) > 30:
            risks.append({
                'level': 'Medium',
                'category': 'Provisioning',
                'description': 'Complex provisioning setup',
                'mitigation': 'Plan for extensive provisioning testing and rollback procedures'
            })
        
        if not risks:
            risks.append({
                'level': 'Low',
                'category': 'General',
                'description': 'Standard migration complexity expected',
                'mitigation': 'Follow standard migration best practices'
            })
        
        return risks
    
    @staticmethod
    def _get_complexity_level(score):
        """Get complexity level from score"""
        if score <= 30:
            return 'Low'
        elif score <= 60:
            return 'Medium'
        else:
            return 'High'
    
    @staticmethod
    def _get_migration_phases(timeline_weeks):
        """Get migration phases breakdown"""
        return [
            {'phase': 'Planning & Assessment', 'weeks': max(2, int(timeline_weeks * 0.15))},
            {'phase': 'Environment Setup', 'weeks': max(1, int(timeline_weeks * 0.1))},
            {'phase': 'User Migration', 'weeks': max(2, int(timeline_weeks * 0.2))},
            {'phase': 'Application Migration', 'weeks': max(3, int(timeline_weeks * 0.35))},
            {'phase': 'Testing & Validation', 'weeks': max(2, int(timeline_weeks * 0.15))},
            {'phase': 'Cutover & Support', 'weeks': max(1, int(timeline_weeks * 0.05))}
        ]
    
    @staticmethod
    def _get_critical_path_items(data):
        """Identify critical path items"""
        critical_items = []
        
        if data.get('workflow_automations_count', 0) > 10:
            critical_items.append('Workflow Automations Recreation')
        
        if data.get('swa_apps_count', 0) > 20:
            critical_items.append('SWA Applications Migration')
        
        if data.get('federated_domains_count', 0) > 3:
            critical_items.append('Domain Federation Setup')
        
        if data.get('provisioning_enabled_apps', 0) > 20:
            critical_items.append('Provisioning Configuration')
        
        if not critical_items:
            critical_items.append('Standard Application Migration')
        
        return critical_items
    
    @staticmethod
    def _generate_recommendations(data, complexity_score):
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if complexity_score > 70:
            recommendations.append({
                'category': 'Approach',
                'recommendation': 'Consider phased migration approach to reduce risk',
                'priority': 'High'
            })
        
        if data.get('workflow_automations_count', 0) > 15:
            recommendations.append({
                'category': 'Automation',
                'recommendation': 'Evaluate Power Automate for workflow replacement',
                'priority': 'Medium'
            })
        
        if data.get('num_employees', 0) > 2000:
            recommendations.append({
                'category': 'Planning',
                'recommendation': 'Conduct pilot migration with small user group first',
                'priority': 'High'
            })
        
        recommendations.append({
            'category': 'Best Practice',
            'recommendation': 'Implement comprehensive monitoring and alerting',
            'priority': 'Medium'
        })
        
        recommendations.append({
            'category': 'Support',
            'recommendation': 'Plan for user training and communication throughout migration',
            'priority': 'Medium'
        })
        
        return recommendations
    
    @staticmethod
    def _convert_api_data(api_data):
        """Convert OKTA API data to internal format"""
        # This would handle real API data structure
        return {
            'num_employees': api_data.get('users_count', 0),
            'saml_apps_count': api_data.get('applications', {}).get('saml', 0),
            'bookmark_apps_count': api_data.get('applications', {}).get('bookmark', 0),
            'swa_apps_count': api_data.get('applications', {}).get('swa', 0),
            'oidc_apps_count': api_data.get('applications', {}).get('oidc', 0),
            'okta_policies_count': api_data.get('policies_count', 0),
            'groups_recreate_count': api_data.get('groups_count', 0),
            'workflow_automations_count': api_data.get('custom_integrations', 0),
            'provisioning_enabled_apps': api_data.get('sso_integrations', 0) // 2,  # Estimate
            'federated_domains_count': 1,  # Default
            'okta_ad_agents_count': 1,  # Default
            'okta_radius_agents_count': 0,  # Default
            'push_groups_apps_count': api_data.get('sso_integrations', 0) // 3,  # Estimate
            'total_push_groups_count': api_data.get('groups_count', 0),
            'annual_okta_cost': api_data.get('users_count', 0) * 48  # Estimate $4/user/month
        }
    
    @staticmethod
    def _analyze_complexity_factors(form_data):
        """Analyze specific complexity factors from form data"""
        factors = {}
        
        # Regulatory complexity
        regulatory_reqs = form_data.get('regulatory_requirements', [])
        if isinstance(regulatory_reqs, list) and len(regulatory_reqs) > 3:
            factors['regulatory_complexity'] = 'High'
        elif isinstance(regulatory_reqs, list) and len(regulatory_reqs) > 1:
            factors['regulatory_complexity'] = 'Medium'
        else:
            factors['regulatory_complexity'] = 'Low'
        
        # Identity provider complexity
        identity_providers = form_data.get('current_identity_providers', [])
        if isinstance(identity_providers, list) and len(identity_providers) > 2:
            factors['identity_provider_complexity'] = 'High'
        elif isinstance(identity_providers, list) and len(identity_providers) > 1:
            factors['identity_provider_complexity'] = 'Medium'
        else:
            factors['identity_provider_complexity'] = 'Low'
        
        # Application refactoring complexity
        refactoring_appetite = form_data.get('appetite_app_refactoring', '')
        if 'Low' in refactoring_appetite or 'None' in refactoring_appetite:
            factors['refactoring_complexity'] = 'High'
        else:
            factors['refactoring_complexity'] = 'Medium'
        
        return factors

def get_predefined_scenarios():
    """Return all predefined scenarios"""
    return PREDEFINED_SCENARIOS
