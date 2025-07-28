import json

    def export_conflicts_to_json(self, filename="conflicts_export.json"):
        data = [{
            "id": conflict.id,
            "description": conflict.description,
            "parties": conflict.parties,
            "severity": conflict.severity,
            "status": conflict.status,
            "created_at": conflict.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "resolution_notes": conflict.resolution_notes
        } for conflict in self.conflicts]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"📤 Conflicts exported to '{filename}'.\n")

    def sort_conflicts_by_date(self, descending=True):
        self.conflicts.sort(key=lambda c: c.created_at, reverse=descending)
        print(f"📅 Conflicts sorted by creation date ({'newest first' if descending else 'oldest first'}).\n")

    def check_duplicate(self, description, parties):
        for conflict in self.conflicts:
            if conflict.description == description and set(conflict.parties) == set(parties):
                print("⚠️ Duplicate conflict detected!\n")
                return True
        print("✅ No duplicate found.\n")
        return False

    def get_recent_conflicts(self, days=7):
        print(f"🕒 Conflicts from the last {days} days:")
        threshold = datetime.datetime.now() - datetime.timedelta(days=days)
        found = False
        for conflict in self.conflicts:
            if conflict.created_at >= threshold:
                print(conflict)
                print("-" * 40)
                found = True
        if not found:
            print("📭 No recent conflicts found.\n")

    def list_unresolved_conflicts(self):
        print("🧨 Unresolved Conflicts (Open/Reopened):")
        found = False
        for conflict in self.conflicts:
            if conflict.status in ["Open", "Reopened"]:
                print(conflict)
                print("-" * 40)
                found = True
        if not found:
            print("😎 No unresolved conflicts!\n")
