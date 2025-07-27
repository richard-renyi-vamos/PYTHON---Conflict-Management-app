import datetime

class Conflict:
    def __init__(self, description, parties, severity):
        self.id = id(self)
        self.description = description
        self.parties = parties
        self.severity = severity
        self.status = "Open"
        self.created_at = datetime.datetime.now()
        self.resolution_notes = ""

    def update_status(self, new_status, notes=""):
        self.status = new_status
        self.resolution_notes = notes

    def __str__(self):
        return (f"Conflict ID: {self.id}\n"
                f"Description: {self.description}\n"
                f"Parties: {', '.join(self.parties)}\n"
                f"Severity: {self.severity}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Resolution Notes: {self.resolution_notes}\n")


class ConflictManager:
    def __init__(self):
        self.conflicts = []

    def add_conflict(self, description, parties, severity):
        conflict = Conflict(description, parties, severity)
        self.conflicts.append(conflict)
        print("✅ Conflict added successfully.\n")

    def list_conflicts(self, filter_status=None):
        print("📋 Listing Conflicts:")
        for conflict in self.conflicts:
            if filter_status is None or conflict.status == filter_status:
                print(conflict)
                print("-" * 40)

    def resolve_conflict(self, conflict_id, notes):
        for conflict in self.conflicts:
            if conflict.id == conflict_id:
                conflict.update_status("Resolved", notes)
                print("🎯 Conflict resolved!\n")
                return
        print("❌ Conflict ID not found.\n")

    def reopen_conflict(self, conflict_id):
        for conflict in self.conflicts:
            if conflict.id == conflict_id and conflict.status == "Resolved":
                conflict.update_status("Reopened", "Reopened for further discussion.")
                print("🔁 Conflict reopened.\n")
                return
        print("⚠️ Conflict not found or not resolved.\n")

    def delete_conflict(self, conflict_id):
        for conflict in self.conflicts:
            if conflict.id == conflict_id:
                self.conflicts.remove(conflict)
                print("🗑️ Conflict deleted.\n")
                return
        print("❌ Conflict ID not found.\n")

    def search_by_party(self, party_name):
        print(f"🔍 Searching conflicts involving '{party_name}':")
        found = False
        for conflict in self.conflicts:
            if party_name in conflict.parties:
                print(conflict)
                print("-" * 40)
                found = True
        if not found:
            print("😕 No conflicts found involving this party.\n")

    def filter_by_severity(self, severity_level):
        print(f"⚠️ Conflicts with severity '{severity_level}':")
        found = False
        for conflict in self.conflicts:
            if conflict.severity.lower() == severity_level.lower():
                print(conflict)
                print("-" * 40)
                found = True
        if not found:
            print("😕 No conflicts found with this severity level.\n")

    def get_statistics(self):
        stats = {"Open": 0, "Resolved": 0, "Reopened": 0}
        for conflict in self.conflicts:
            stats[conflict.status] = stats.get(conflict.status, 0) + 1
        print("📊 Conflict Statistics:")
        for status, count in stats.items():
            print(f"{status}: {count}")
        print()


# 🎮 Example Usage
if __name__ == "__main__":
    manager = ConflictManager()

    manager.add_conflict("Miscommunication about project deadline", ["Alice", "Bob"], "High")
    manager.add_conflict("Disagreement on design choice", ["Team A", "Team B"], "Medium")
    manager.add_conflict("Budget allocation issue", ["Alice", "Finance Dept."], "High")

    manager.list_conflicts()

    # Resolve a conflict
    first_conflict_id = manager.conflicts[0].id
    manager.resolve_conflict(first_conflict_id, "Held a meeting and clarified responsibilities.")

    # Reopen it
    manager.reopen_conflict(first_conflict_id)

    # Delete a conflict
    second_conflict_id = manager.conflicts[1].id
    manager.delete_conflict(second_conflict_id)

    # Search
    manager.search_by_party("Alice")

    # Filter
    manager.filter_by_severity("High")

    # Stats
    manager.get_statistics()
