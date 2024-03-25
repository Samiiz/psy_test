from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union, List
from crud import sql
from schemas import staff
import database