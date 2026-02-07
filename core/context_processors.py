"""
I keep all shared Tailwind UI classes here so the design stays consistent
and easy to change across the whole app.
"""

def ui(request):
    return {
        "UI": {
            # Buttons
            "btn_primary": (
                "inline-flex items-center justify-center rounded-lg "
                "bg-slate-900 px-4 py-2 text-sm font-medium text-white "
                "hover:bg-slate-800 focus:outline-none focus:ring-2 "
                "focus:ring-slate-400 focus:ring-offset-2"
            ),
            "btn_secondary": (
                "inline-flex items-center justify-center rounded-lg "
                "border border-slate-200 bg-white px-4 py-2 text-sm "
                "text-slate-700 hover:bg-slate-50 focus:outline-none "
                "focus:ring-2 focus:ring-slate-300 focus:ring-offset-2"
            ),

            # Cards
            "card": (
                "rounded-2xl border border-slate-200 bg-white p-6 shadow-sm"
            ),

            # Inputs
            "input": (
                "w-full rounded-lg border border-slate-300 px-3 py-2 text-sm "
                "focus:border-slate-500 focus:outline-none focus:ring-1 "
                "focus:ring-slate-400"
            ),

            # Section headings
            "h2": "text-xl font-semibold tracking-tight text-slate-900",
            "muted": "text-sm text-slate-500",
        }
    }
