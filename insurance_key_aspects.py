# ============================================
#  AS | Attika Sufyan
#  Cybersecurity Student
#  GitHub: github.com/attikasufyan870-del
#  Course: EC-Council Cybersecurity
#  Topic: Key Aspects of Cyber Insurance
#  Chapter: 3
#  Date: April 2026
# ============================================

def insurance_key_aspects():
    print("=" * 55)
    print("  AS | Attika Sufyan — Insurance Key Aspects Tool")
    print("=" * 55)
    
    print("\n🛡️ Cyber Insurance Key Aspects Checker\n")
    
    print("📋 Key Aspects Select Karo:")
    print("1. Policy Coverage")
    print("2. Exclusions")
    print("3. Premium Calculation")
    print("4. Claims Process")
    
    choice = int(input("\nNumber select karo (1-4): "))
    
    print("\n" + "=" * 55)
    
    if choice == 1:
        print("📄 Policy Coverage — Kya Cover Hota Hai:")
        print("✅ Data Breach — Customer data leak")
        print("✅ Ransomware Attack — Files lock ho jayein")
        print("✅ Business Interruption — Kaam band ho jaye")
        print("✅ Legal Fees — Court cases")
        print("✅ Notification Costs — Customers ko inform karna")
        
    elif choice == 2:
        print("❌ Exclusions — Kya Cover NAHI Hota:")
        print("🚫 Intentional Acts — Khud ki galti")
        print("🚫 War/Terrorism — War attacks")
        print("🚫 Prior Incidents — Pehle se hua attack")
        print("🚫 Unpatched Systems — Update na kiye systems")
        print("🚫 Insider Threats — Employee ki galti")
        
    elif choice == 3:
        print("💰 Premium Calculation — Price Kaise Tay Hoti Hai:")
        print("📊 Factor 1: Business size")
        print("📊 Factor 2: Data sensitivity")
        print("📊 Factor 3: Security measures")
        print("📊 Factor 4: Previous incidents")
        print("📊 Factor 5: Industry type")
        
        # Simple Premium Calculator
        print("\n💵 Premium Calculator:")
        size = int(input("Business size (1=Small, 2=Medium, 3=Large): "))
        security = int(input("Security level (1=Low, 2=Medium, 3=High): "))
        
        base = 1000
        premium = base * size * (4 - security)
        print(f"\n💰 Estimated Annual Premium: ${premium}")
        
    elif choice == 4:
        print("📝 Claims Process — Claim Kaise Karte Hain:")
        print("✅ Step 1: Incident report karo")
        print("✅ Step 2: Insurance company ko inform karo")
        print("✅ Step 3: Evidence collect karo")
        print("✅ Step 4: Claim form bharo")
        print("✅ Step 5: Investigation hogi")
        print("✅ Step 6: Payment milegi")
    
    print("=" * 55)

# Program Start
insurance_key_aspects()
